# SuperNOVA <a href="https://poloclub.github.io/supernova/"><img align="right" src="public/favicon.svg" width="32" height="32"></img></a>


[![Github Actions Status](https://github.com/poloclub/supernova/workflows/build/badge.svg)](https://github.com/poloclub/supernova/actions/workflows/build.yml)
[![license](https://img.shields.io/badge/License-MIT-success)](https://github.com/poloclub/supernova/blob/master/LICENSE)

Design Strategies and Opportunities for Interactive Visualization in Computational Notebooks

<table>
  <tr>
    <td colspan="1"><a href="https://poloclub.github.io/supernova"><img src='https://i.imgur.com/osA5hH3.png'></a></td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td><a href="https://poloclub.github.io/supernova">🚀 Live Demo: Explore 159 notebook visual analytics tools in your browser!</a></td>
    <!-- <td><a href="https://youtu.be/3eGqTmsStJM">📺 Demo Video</a></td>
    <td><a href="https://youtu.be/l1mr9z1TuAk">👨🏻‍🏫 Conference Talk</a></td>
    <td><a href="https://arxiv.org/abs/2209.09227">📖 Research Paper</a></td> -->
  </tr>
</table>


## Overview

SuperNOVA is an interactive browser to help researchers explore existing notebook VA tools and search for design inspiration and implementation references. Anyone can easily add new notebook VA tools to this open-source explorer.

## SuperNOVA Details

Computational notebooks such as Jupyter Notebook have become data scientists' de facto programming environments. Many visualization researchers and practitioners have developed interactive visualization tools that support notebooks. However, little is known about the appropriate design of visual analytics (VA) tools in notebooks. To bridge this critical research gap, we investigate the design strategies in this space by analyzing 148 notebook VA tools and their users' feedback. SuperNOVA is an interactive browsers to help researchers explore the landscape of notebook VA tools and search for related work.

## Live Demo

For a live web demo of SuperNOVA, visit: <https://poloclub.github.io/supernova/>

## How to add an entry to SuperNOVA

If your open-source interactive VA tool is also compatible in notebooks, please submit a [pull request](https://github.com/poloclub/supernova/pulls) to add your tool to SuperNOVA. You can add your VA tool to the [YAML file](https://github.com/poloclub/supernova/blob/main/src/data/supernova.yaml) with the following steps:

Make sure you have the necessary information for the entry you want to add, including the paper's title, authors, publication year, conference or journal name, DOI or URL, and a brief description of the paper's content.

1. Open the [YAML file](https://github.com/poloclub/supernova/blob/main/src/data/supernova.yaml) where the existing entries are stored.
2. Use the following YAML template, and paste it below the last entry:

```yaml
- bibtex:
  communication: ''
  description:
  githubURL:
  implementation: ''
  layouts: []
  materials: []
  modularity: ''
  name:
  otherURLs: []
  paperURL:
  releaseYear:
  sourceType:
  supportedNotebooks: []
  user: ''
```

3. Replace the values in the new entry with the information you have for the new paper, making sure to keep the same key names for each value.
  - If the VA tool has a BibTeX citation, add it to the `bibtext` field.
  - Provide a brief description of the VA tool in the `description` field (e.g. a paper abstract, the About text from a Github repository).
  - If the VA tool has a GitHub repository add the link to the `githubURL` field.
  - Describe the implementation of the VA tool in the `implementation` field.
  - Include the name of the VA tool in the `name` field.
  - If the VA tool has other relevant URLs, add those to the `otherURLs` field.
  - If the VA tool is from an academic paper, add a link to the paper in the `paperURL` field.
  - Include the year the VA tool was released in the `releaseYear` field.
  - If the VA tool is from an academic paper, add "paper" to the `sourceType` field. If the VA tool is an open-source system, add "package" to the `sourceType` field.
  - If the VA tool is compatible with a specific notebook platform, list the platform in the `supportedNotebooks` field (e.g. Jupyter, Colab, etc.).

4. Save the file and make a pull request to the repository.

## Data Collection

Code for data collection and cleaned GitHub issues are at [`./metadata`](./metadata).

## Credits

SuperNOVA is created by <a href='https://zijie.wang/' target='_blank'>Jay Wang</a>, <a href='https://www.davidmunechika.com' target='_blank'>David Munechika</a>, <a href='http://www.seongmin.xyz' target='_blank'>Seongmin Lee</a>, and <a href='' target='_blank'>Polo Chau</a>.

<!-- ## Citation

```bibTeX

``` -->

## License

The code is available under the [MIT License](https://github.com/poloclub/supernova/blob/master/LICENSE).

## Contact

If you have any questions, feel free to [open an issue](https://github.com/poloclub/supernova/issues/new) or contact [Jay Wang](https://zijie.wang).
