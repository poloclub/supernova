# SuperNOVA <a href="https://poloclub.github.io/supernova/"><img align="right" src="public/favicon.svg" width="30" height="30"></img></a>


[![Github Actions Status](https://github.com/poloclub/supernova/workflows/build/badge.svg)](https://github.com/poloclub/supernova/actions/workflows/build.yml)
[![license](https://img.shields.io/badge/License-MIT-success)](https://github.com/poloclub/supernova/blob/master/LICENSE)

Design Strategies and Opportunities for Interactive Visualization in Computational Notebooks

<table>
  <tr>
    <td colspan="1"><a href="https://poloclub.github.io/supernova"><img src='https://i.imgur.com/wy2NbdR.png'></a></td>
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

SuperNOVA is an interactive tool to help researchers explore existing notebook VA tools and search for design inspiration and implementation references. Anyone can easily add new notebook VA tools to this open-source explorer.

## SuperNOVA Details

Computational notebooks such as Jupyter Notebook have become data scientists' de facto programming environments. Many visualization researchers and practitioners have developed interactive visualization tools that support notebooks. However, little is known about the appropriate design of visual analytics (VA) tools in notebooks. To bridge this critical research gap, we investigate the design strategies in this space by analyzing 159 notebook VA tools and their users' feedback. SuperNOVA is an interactive browsers to help researchers explore the landscape of notebook VA tools and search for related work.

## Live Demo

For a live web demo of SuperNOVA, visit: <https://poloclub.github.io/supernova/>

## How to add an entry to SuperNOVA

To add a new notebook VA tool into the SuperNOVA collection, please submit a [pull request](https://github.com/poloclub/supernova/pulls). You can add your VA tool to the [YAML file](https://github.com/poloclub/supernova/blob/main/src/data/supernova.yaml) with the following steps:

Make sure you have the necessary information for the entry you want to add, including the tool's title, authors, publication or release year, [conference name], DOI or URL, and a brief description of the paper's content.

1. Open the [YAML file](https://github.com/poloclub/supernova/blob/main/src/data/supernova.yaml) where the existing entries are stored.
2. Use the following YAML template, and paste it below the last entry. For the definition details of each entry, please check out the SuperNOVA paper.

```yaml
- bibtex: ''
  # {string} The bibtex of this entry

  bibtexKey: ''
  # {string} The bibtex key

  communication: ''
  # {'no' | 'one-way' | 'two-way'} VA-notebook communication style

  description: ''
  # {string} A description of the tool, can be the abstract of its paper

  githubURL: ''
  # {string?} GitHub repository URL

  implementation: ''
  # {'ipywidget'| 'extension' | 'html' | 'nova' | 'other-package' | 'custom'} Implementation strategy

  layouts: ''
  # {'on-demand' | 'always-on'} The display style of the VA tool

  materials: ['']
  # {['runtime' | 'code' | 'external']} Types of data this VA tool uses

  modularity: ''
  # {'monolithic' | 'modular'} The modularity of this VA tool

  name: ''
  # {string} Name of this tool in lowercase. It has to match the thumbnail file name.

  nameDisplay: ''
  # {string} The name of this tool

  otherURLs: []
  # {string[]?} Other URLs of this tool

  paperURL: ''
  # {string?} Paper URL

  releaseYear: 2023
  # {number} The release/publication year

  sourceType: ''
  # {'paper' | 'package'} If this tool has a related paper, use 'paper'.

  supportedNotebooks: ['']
  # {['jupyter' | 'lab' | 'colab' | 'vscode']} List of supported notebook platforms

  user: ''
  # {'data scientist' | 'scientist' | 'educator'} The main targeted users
```

3. Save a thumbnail image in the [`./public/images/thumbnails/`](./public/images/thumbnails/) directory. Please compress the image and make sure the file size is smaller than 100kb.
4. Submit a pull request to the repository.

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
