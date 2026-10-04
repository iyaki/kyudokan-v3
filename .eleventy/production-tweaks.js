import postcss from 'postcss'
import postcssPresetEnv from 'postcss-preset-env'
import cssnano from 'cssnano'
import htmlSyntax from 'postcss-html'
import { minify as minifyHtml } from 'html-minifier-terser'
import { load as cheerioLoad } from 'cheerio'

// ponytail: portado de iyaki.github.io; exclusiones above-fold propias (crest y shisas)
function getPostCss() {
	const postCssConfig = [
		postcssPresetEnv({
			minimumVendorImplementations: 3,
			features: {
				'nesting-rules': true,
			}
		}),
		cssnano(),
	]

	return postcss(postCssConfig)
}

/** @param {import("@11ty/eleventy").UserConfig} eleventyConfig */
export default function (eleventyConfig) {
	eleventyConfig.addTemplateFormats('css')

	eleventyConfig.addExtension('css', {
		outputFileExtension: 'css',

		compile: async (content, from) => {
			return async () => {
				return process.env.ELEVENTY_RUN_MODE === 'build' ?
					(await getPostCss().process(content, { from })).css :
					content
			}
		}
	})

	eleventyConfig.addTransform('minify html', async function(content) {
		if (process.env.ELEVENTY_RUN_MODE !== 'build') {
			return content
		}

		if( !(this.page.outputPath && this.page.outputPath.endsWith(".html")) ) {
			return content
		}

		// Minifica el CSS inline (attrs style y <style>) junto con el HTML
		content = (
			await getPostCss()
				.process(content, {from: this.inputPath, syntax: htmlSyntax})
		).css

		content = await minifyHtml(content, {
			minifyJS: true,
			removeComments: true,
			removeRedundantAttributes: true,
			removeScriptTypeAttributes: true,
			removeStyleLinkTypeAttributes: true,
		})

		return content
	})

	eleventyConfig.addTransform('lazy load images', async function(content) {
		if (process.env.ELEVENTY_RUN_MODE !== 'build') {
			return content
		}

		if( !(this.page.outputPath && this.page.outputPath.endsWith(".html")) ) {
			return content
		}

		const $ = cheerioLoad(content, null, false)
		// crest y shisas son above-fold: lazy ahí empeora el LCP
		$('img:not([loading]):not(.crest):not(.shisa)').attr('loading', 'lazy')
		return $.html()
	})

	eleventyConfig.addTransform('noopener noreferrer', async function(content) {
		if (process.env.ELEVENTY_RUN_MODE !== 'build') {
			return content
		}

		if( !(this.page.outputPath && this.page.outputPath.endsWith(".html")) ) {
			return content
		}

		const $ = cheerioLoad(content, null, false)
		$('a[target="_blank"]').each((_, el) => {
			const $el = $(el)
			const rel = $el.attr('rel') || ''
			if (!rel.includes('noopener')) {
				$el.attr('rel', (rel ? rel + ' ' : '') + 'noopener noreferrer')
			}
		})
		return $.html()
	})

	eleventyConfig.addTransform('minify xml', async function(content) {
		if (process.env.ELEVENTY_RUN_MODE !== 'build') {
			return content
		}

		if( !(this.page.outputPath && this.page.outputPath.endsWith(".xml")) ) {
			return content
		}

		const xmlMinifier = await import('minify-xml')

		return xmlMinifier.minify(content)
	})
}
