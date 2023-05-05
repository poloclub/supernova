# SuperNOVA <a href="https://poloclub.github.io/supernova/"><img align="right" src="public/android-chrome-192x192.png" width="30" height="30"></img></a>


[![Github Actions Status](https://github.com/poloclub/supernova/workflows/build/badge.svg)](https://github.com/poloclub/supernova/actions/workflows/build.yml)
[![license](https://img.shields.io/badge/License-MIT-blue)](https://github.com/poloclub/supernova/blob/master/LICENSE)
[![arxiv badge](https://img.shields.io/badge/arXiv-2305.03039-red)](http://arxiv.org/abs/2305.03039)

Design Strategies and Opportunities for Interactive Visualization in Computational Notebooks

<table>
  <tr>
    <td colspan="2"><a href="https://poloclub.github.io/supernova"><img src='https://i.imgur.com/wy2NbdR.png'></a></td>
  </tr>
  <tr></tr>
  <tr align="center">
    <td><a href="https://poloclub.github.io/supernova">🚀 Live Demo: Explore 161 notebook visual analytics tools in your browser!</a></td>
    <!-- <td><a href="https://youtu.be/3eGqTmsStJM">📺 Demo Video</a></td>
    <td><a href="https://youtu.be/l1mr9z1TuAk">👨🏻‍🏫 Conference Talk</a></td> -->
    <td><a href="https://arxiv.org/abs/2305.03039">📖 Research Paper</a></td>
  </tr>
</table>

## Overview

SuperNOVA is an interactive tool to help researchers explore existing notebook VA tools and search for design inspiration and implementation references. Anyone can easily add new notebook VA tools to this open-source explorer.

## SuperNOVA Details

Computational notebooks such as Jupyter Notebook have become data scientists' de facto programming environments. Many visualization researchers and practitioners have developed interactive visualization tools that support notebooks. However, little is known about the appropriate design of visual analytics (VA) tools in notebooks. To bridge this critical research gap, we investigate the design strategies in this space by analyzing 159 notebook VA tools and their users' feedback. SuperNOVA is an interactive browsers to help researchers explore the landscape of notebook VA tools and search for related work.

## Live Demo

For a live web demo of SuperNOVA, visit: <https://poloclub.github.io/supernova/>.

## How to add an entry to SuperNOVA

To add a new notebook VA tool into the SuperNOVA collection, please submit a [pull request](https://github.com/poloclub/supernova/pulls). You can add your VA tool to the [YAML file](https://github.com/poloclub/supernova/blob/main/src/data/supernova.yaml) with the following steps:

Make sure you have the necessary information for the entry you want to add, including the tool's title, authors, publication or release year, [conference name], DOI or URL, and a brief description of the paper's content.

1. Open the [YAML file](https://github.com/poloclub/supernova/blob/main/src/data/supernova.yaml) where the existing entries are stored.
2. Use the following YAML template, and paste it below the last entry. For the definition details of each entry, please check out the SuperNOVA paper.

```yaml
-
  # {string} The bibtex of this entry
  bibtex: ''

  # {string} The bibtex key
  bibtexKey: ''

  # {'no' | 'one-way' | 'two-way'} VA-notebook communication style
  communication: ''

  # {string} A description of the tool, can be the abstract of its paper
  description: ''

  # {string?} GitHub repository URL
  githubURL: ''

  # {'ipywidget'| 'extension' | 'html' | 'nova' | 'other-package' | 'custom'} Implementation strategy
  implementation: ''

  # {'on-demand' | 'always-on'} The display style of the VA tool
  layouts: ''

  # {['runtime' | 'code' | 'external']} Types of data this VA tool uses
  materials: ['']

  # {'monolithic' | 'modular'} The modularity of this VA tool
  modularity: ''

  # {string} Name of this tool in lowercase. It has to match the thumbnail file name.
  name: ''

  # {string} The name of this tool
  nameDisplay: ''

  # {string[]?} Other URLs of this tool
  otherURLs: []

  # {string?} Paper URL
  paperURL: ''

  # {number} The release/publication year
  releaseYear: 2023

  # {'paper' | 'package'} If this tool has a related paper, use 'paper'.
  sourceType: ''

  # {['jupyter' | 'lab' | 'colab' | 'vscode']} List of supported notebook platforms
  supportedNotebooks: ['']

  # {'data scientist' | 'scientist' | 'educator'} The main targeted users
  user: ''
```

3. Save a thumbnail image in the [`./public/images/thumbnails/`](./public/images/thumbnails/) directory. Please resize the image so that both width and height are smaller than 300px and compress the image to be smaller than 20kb.
4. Submit a [pull request](https://github.com/poloclub/supernova/pulls) to this repository.

## Data Collection

Code for data collection and cleaned GitHub issues are at [`./metadata`](./metadata).

## Credits

SuperNOVA is created by <a href='https://zijie.wang/' target='_blank'>Jay Wang</a>, <a href='https://www.davidmunechika.com' target='_blank'>David Munechika</a>, <a href='http://www.seongmin.xyz' target='_blank'>Seongmin Lee</a>, and <a href='' target='_blank'>Polo Chau</a>.

## Citation

```bibTeX
@article{wangSuperNOVADesignStrategies2023,
  title = {{{SuperNOVA}}: {{Design Strategies}} and {{Opportunities}} for {{Interactive Visualization}} in {{Computational Notebooks}}},
  shorttitle = {{{SuperNOVA}}},
  author = {Wang, Zijie J. and Munechika, David and Lee, Seongmin and Chau, Duen Horng},
  year = {2023},
  url = {http://arxiv.org/abs/2305.03039},
  urldate = {2023-05-05},
  archiveprefix = {arxiv},
  journal = {arXiv 2305.03039}
}
```

## License

The code is available under the [MIT License](https://github.com/poloclub/supernova/blob/master/LICENSE).

## Contact

If you have any questions, feel free to [open an issue](https://github.com/poloclub/supernova/issues/new) or contact [Jay Wang](https://zijie.wang).
