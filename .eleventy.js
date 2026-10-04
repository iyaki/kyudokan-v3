/** @param {import("@11ty/eleventy").UserConfig} eleventyConfig */
export default function (eleventyConfig) {
	eleventyConfig.addPassthroughCopy('src/assets')
	eleventyConfig.addPassthroughCopy('src/gusuku.css')
	eleventyConfig.addPassthroughCopy('src/_headers')
	eleventyConfig.addPassthroughCopy('src/_redirects')

	return {
		dir: {
			input: 'src',
		},
	}
}
