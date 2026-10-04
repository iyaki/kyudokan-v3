import ProductionTweaks from './.eleventy/production-tweaks.js'

/** @param {import("@11ty/eleventy").UserConfig} eleventyConfig */
export default function (eleventyConfig) {
	eleventyConfig.addPlugin(ProductionTweaks)

	eleventyConfig.addPassthroughCopy('src/assets')
	eleventyConfig.addPassthroughCopy('src/_headers')
	eleventyConfig.addPassthroughCopy('src/_redirects')

	return {
		dir: {
			input: 'src',
		},
	}
}
