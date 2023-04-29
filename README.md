# NOVA

[![Github Actions Status](https://github.com/poloclub/nova/workflows/build/badge.svg)](https://github.com/poloclub/nova/actions/workflows/build.yml)
[![license](https://img.shields.io/badge/License-MIT-brightgreen)](https://github.com/poloclub/nova/blob/master/LICENSE)
[![pypi](https://img.shields.io/pypi/v/nova-graph?color=blue)](https://pypi.python.org/pypi/nova-graph)
[![Lite](https://gist.githubusercontent.com/xiaohk/9b9f7c8fa162b2c3bc3251a5c9a799b2/raw/a7fca1d0a2d62c2b49f60c0217dffbd0fe404471/lite-badge-launch-small.svg)](https://poloclub.github.io/nova/notebook)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/poloclub/nova/master?urlpath=lab/tree/svelte-ts/notebook-widget/example/nova-graph.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WPT-pjO4-qNdD-UYwrFk7DVwAl2XrHBB?usp=sharing)
[![arxiv badge](https://img.shields.io/badge/arXiv-2205.03963-red)](https://arxiv.org/abs/2205.03963)
<!-- [![DOI:10.1145/3491101.3519653](https://img.shields.io/badge/DOI-10.1145/3491101.3519653-blue)](https://doi.org/10.1145/3491101.3519653) -->

A simple and flexible method to create notebook-ready visual analytics tools!

<!-- <table>
  <tr>
    <td colspan="1"><img src='https://i.imgur.com/FtmHafo.png'></td>
  </tr>
  <tr></tr>
  <tr>
    <td><a href="https://youtu.be/eMlTtloGyho">👨🏻‍🏫 Talk</a></td>
    <td><a href="https://youtu.be/OKaPmEBzEX0">📺 Video</a></td>
    <td><a href="https://arxiv.org/abs/2202.11086">📖 "StickyLand: breaking the linear presentation of computational Notebooks"</a></td>
  </tr>
</table> -->

|<img src='https://i.imgur.com/tlkVvjt.png'>|
|:---:|
|<a href="https://arxiv.org/abs/2205.03963">"NOVA: A Practical Method for Creating Notebook-Ready Visual Analytics"</a>|

## Overview

NOVA is a simple and flexible method to adapt existing web-based visual analytics (VA) tools to support computational notebooks. Web apps are a popular medium for developing interactive visualization systems that users can access in their web browsers. NOVA converts web apps developed with diverse web technologies, such as programming languages and frameworks, to notebook widgets that end-users can easily install and use in different notebook environments.

## NOVA Details

There are three simple steps to apply NOVA:

1. Convert the VA tool into a single HTML file
2. Design Python wrapper API
3. Publish the VA widget in a software repository

The implementation details of each step vary depending on the VA tool's development stack. We provide three detailed examples with a toy VA tool to demonstrate how to apply NOVA on VA systems developed with diverse web technologies.

You can navigate to the folders below and read their individual `README.md` files for implementation details.

|Example|Web Development Stack|Bundler|Comment|
|:---:|:---:|:---:|:---:|
|[`svelte-ts`](./svelte-ts/)|[Svelte](https://svelte.dev) + [SCSS](https://sass-lang.com) + [TypeScript](https://www.typescriptlang.org)|[Vite](https://vitejs.dev)|It also explains how to set up a demo page|
|[`react-js`](./react-js/)|[React](https://reactjs.org)|[Webpack](https://webpack.js.org)||
|[`vanilla-js`](./vanilla-js/)|HTML + CSS + JavaScript|[Rollup](https://rollupjs.org/guide/en/)||

## Live Demo

For a live web demo of this toy VA tool, visit: <https://poloclub.github.io/nova>

You can also directly try out the notebook widget in your favorite computational notebooks (e.g. Jupyter Notebook/Lab, Google Colab, and VS Code Notebook).

Check out three live notebook demos below.

|Jupyter Lite|Binder|Google Colab|
|:---:|:---:|:---:|
|[![Lite](https://gist.githubusercontent.com/xiaohk/9b9f7c8fa162b2c3bc3251a5c9a799b2/raw/a7fca1d0a2d62c2b49f60c0217dffbd0fe404471/lite-badge-launch-small.svg)](https://poloclub.github.io/nova/notebook)|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/poloclub/nova/master?urlpath=lab/tree/svelte-ts/notebook-widget/example/nova-graph.ipynb)|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WPT-pjO4-qNdD-UYwrFk7DVwAl2XrHBB?usp=sharing)|

## Open-source VA tools that use NOVA

If your open-source VA tool also applies NOVA to create notebook widgets, please submit a [pull request](https://github.com/poloclub/nova/pulls) to add your tool on top of this table :)

|Name|Description|
|:---|:---|
[Visual Auditor](https://github.com/poloclub/visual-auditor)|Interactive visualization system for identifying and understanding biases in machine learning models.|
[TimberTrek](https://github.com/poloclub/timbertrek)|Visual analytics tool to help data scientists curate decision trees that align with their knowledge and values.
[GAM Changer](https://github.com/interpretml/gam-changer)|Interactive visualization tool to help domain experts and data scientist easily and responsibly edit Generalized Additive Models (GAMs)|

## Credits

NOVA is created by <a href='https://zijie.wang/' target='_blank'>Jay Wang</a>, <a href='https://www.linkedin.com/in/dmunechika' target='_blank'>David Munechika</a>, <a href='http://www.seongmin.xyz' target='_blank'>Seongmin Lee</a>, and <a href='' target='_blank'>Polo Chau</a>.

## Citation

```bibTeX
@article{wangNOVAPracticalMethod2022,
  title = {{{NOVA}}: {{A Practical Method}} for {{Creating Notebook-Ready Visual Analytics}}},
  shorttitle = {{{NOVA}}},
  author = {Wang, Zijie J. and Munechika, David and Lee, Seongmin and Chau, Duen Horng},
  year = {2022},
  month = may,
  journal = {arXiv:2205.03963 [cs]},
  archiveprefix = {arXiv}
}
```

## License

The code is available under the [MIT License](https://github.com/poloclub/nova/blob/master/LICENSE).

## Contact

If you have any questions, feel free to [open an issue](https://github.com/poloclub/nova/issues/new) or contact [Jay Wang](https://zijie.wang).
