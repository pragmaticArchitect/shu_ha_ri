import type {Config} from '@docusaurus/types';
import {themes as prismThemes} from 'prism-react-renderer';

const config: Config = {
  title: 'HDIP',
  tagline: 'Holistic Data, Information and Intelligence Platform',
  favicon: 'img/hdip/logo.svg',

  future: {
    v4: true,
  },

  url: 'https://hdip.kivanura.org',
  baseUrl: '/',
  organizationName: 'pragmaticArchitect',
  projectName: 'shu_ha_ri',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  markdown: {
    mermaid: true,
  },

  themes: ['@docusaurus/theme-mermaid'],

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      },
    ],
  ],

  themeConfig: {
    image: 'img/hdip/logo.svg',
    navbar: {
      title: 'HDIP',
      logo: {
        alt: 'HDIP logo',
        src: 'img/hdip/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'hdipSidebar',
          position: 'left',
          label: 'Docs',
        },
        {
          to: '/docs/architecture/hdip-cla-0.1-programme',
          label: 'HDIP-CLA 0.1',
          position: 'left',
        },
        {
          href: 'https://github.com/pragmaticArchitect/shu_ha_ri',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'HDIP',
          items: [
            {label: 'Introduction', to: '/docs/introduction'},
            {label: 'HDIP-CLA 0.1', to: '/docs/architecture/hdip-cla-0.1-programme'},
          ],
        },
        {
          title: 'Related KivaNura Work',
          items: [
            {label: 'BPS', href: 'https://bps.kivanura.org'},
          ],
        },
        {
          title: 'Source',
          items: [
            {label: 'GitHub', href: 'https://github.com/pragmaticArchitect/shu_ha_ri'},
          ],
        },
      ],
      copyright: `Copyright © 2019-${new Date().getFullYear()} KivaNura.org`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  },
};

export default config;
