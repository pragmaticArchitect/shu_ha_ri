// INFOPS P01 Stage 2 research draft. No canonical family qualification is defined here.
const config = {
  title: 'Information Product Specification',
  tagline: 'INFOPS — governed Information Product specification',
  favicon: 'img/favicon.svg',
  url: process.env.SITE_URL || 'https://example.org',
  baseUrl: process.env.BASE_URL || '/',
  organizationName: 'YOUR_GITHUB_ORG',
  projectName: 'YOUR_REPOSITORY_NAME', // Replace with actual GitHub repository name.
  onBrokenLinks: 'throw',
  markdown: {hooks: {onBrokenMarkdownLinks: 'warn'}},
  trailingSlash: false,
  i18n: {defaultLocale: 'en', locales: ['en']},
  presets: [
    ['classic', {
      docs: {sidebarPath: require.resolve('./sidebars.js'), editUrl: undefined, routeBasePath: 'docs'},
      blog: false,
      theme: {customCss: require.resolve('./src/css/custom.css')},
      sitemap: {changefreq: 'weekly', priority: 0.6},
    }],
  ],
  themeConfig: {
    navbar: {
      title: 'INFOPS',
      logo: {alt: 'INFOPS', src: 'img/infops-mark.svg'},
      items: [
        {to: '/docs/intro', label: 'Specification', position: 'left'},
        {to: '/docs/infopch/overview', label: 'Characteristics', position: 'left'},
        {to: '/docs/pmdd/overview', label: 'PMDD', position: 'left'},
        {to: '/INFOPCH-PMDD-guidance', label: 'Agent Guidance', position: 'left'},
        {to: '/docs/integration/hdip-upos', label: 'HDIP & UPOS', position: 'left'},
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {title: 'Explore', items: [
          {label: 'Start here', to: '/docs/intro'},
          {label: 'INFOPS roadmap', to: '/docs/specification/roadmap'},
          {label: 'Release status', to: '/docs/specification/status'},
        ]},
        {title: 'Assessment', items: [
          {label: 'INFOPCH', to: '/docs/infopch/overview'},
          {label: 'PMDD', to: '/docs/pmdd/overview'},
          {label: 'Agent guidance', to: '/INFOPCH-PMDD-guidance'},
        ]},
      ],
      copyright: 'KivaNura / Kaizen — licensing and publication terms pending an explicit governance decision.',
    },
    prism: {additionalLanguages: ['json','python','yaml','bash']},
  },
};
module.exports = config;
