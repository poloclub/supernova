import requests

access_token = '{GITHUB ACCESS TOKEN}'

repos = [
    'agermanidis/pigeon',
    'Autodesk/notebook-molecular-visualization',
    'bmabey/pyLDAvis',
    'bqplot/bqplot',
    'carlos-gg/hciplot',
    'centreborelli/pypotree',
    'potree/potree/',
    'cmudig/AutoProfiler',
    'cuemacro/chartpy',
    'dssg/aequitas',
    'facebookresearch/hiplot',
    'finos/perspective',
    'google/brax',
    'graphistry/pygraphistry',
    'interpretml/interpret',
    'interpretml/interpret-community',
    'ipyannotate/ipyannotate',
    'jessevig/bertviz',
    'koaning/whatlies',
    'merqurio/neo4jupyter',
    'mwouts/itables',
    'PatrikHlobil/Pandas-Bokeh',
    'poliastro/czml3',
    'poloclub/visual-auditor',
    'python-visualization/folium',
    'Quantomatic/pyzx',
    'tensorflow/model-analysis',
    'tensorflow/tensorboard'
    'keplergl/kepler.gl',
    'iseekwonderful/PyPathway',
    'isl-org/Open3D',
    'facebook/Ax',
    'apache/beam',
    'catboost/catboost',
    'CQCL/pytket',
    'sfu-db/dataprep',
    'tkrabel/bamboolib',
    'GeoscienceAustralia/dea-notebooks',
    'enthought/mayavi',
    'lightkurve/lightkurve',
    'voxel51/fiftyone',
    'eli5-org/eli5',
    'zakandrewking/escher',
    'keras-team/keras',
    'flexxui/flexx',
    'GateNLP/python-gatenlp',
    'holoviz/geoviews',
    'intake/intake',
    'cytoscape/cytoscape.js',
    'microsoft/LightGBM',
    'MaartenGr/BERTopic',
    'jupyter-incubator/sparkmagic'
    'executablebooks/MyST-NB',
    'nilearn/nilearn',
    'QuSTaR/kaleidoscope',
    'holoviz/panel',
    'pixiedust/pixiedust',
    'plotly/dash',
    'cytoscape/py2cytoscape',
    'pycaret/pycaret',
    'pydgrid/pydgrid',
    'InsightLab/PyMove',
    'intuitivetextmining/d3fdgraph',
    'Elysian01/Data-Purifier',
    'datapane/datapane',
    'igvteam/igv',
    'patrickfuller/imolecule',
    'InsightSoftwareConsortium/itkwidgets',
    'JupyterPhysSciLab/JupyterPiDAQ',
    'sdpython/jyquickhelper',
    'cbouy/mols2grid',
    'ydataai/ydata-profiling',
    'adamerose/PandasGUI',
    'VIDA-NYU/PipelineVis',
    'visgl/deck.gl',
    'hyriver/pygeohydro',
    'quantopian/qgrid',
    'ranaroussi/quantstats',
    'sid-the-coder/QuickDA',
    'microsoft/responsible-ai-toolbox',
    'fbdesignpro/sweetviz',
    'mikedh/trimesh',
    'facebookresearch/vizseq',
    'PAIR-code/what-if-tool',
    'jnowak90/GraVisGUI',
    'slundberg/shap',
    'Mr-Milk/SpatialTis',
    'sandialabs/toyplot',
    'wandb/wandb',
    'nengo/nengo',
    'pathpy/pathpy'
]

keywords = ['notebook', 'jupyter', 'colab', 'kaggle']

headers = {
    'Authorization': f'token {access_token}'
}

for repo_name in repos:
    url = f'https://api.github.com/repos/{repo_name}/issues?state=all'
    response = requests.get(url, headers=headers)
    repo_name_string = repo_name.replace('/', '_')
    with open(f'{repo_name_string}-issues.txt', 'a') as f:
        f.write(f'{repo_name}\n')

    for issue in response.json():
        try:
            comments_url = issue['comments_url']
            comments_response = requests.get(comments_url, headers=headers)
            comments = comments_response.json()

            title = issue['title']
            description = issue['body']

            if any(keyword in title.lower() for keyword in keywords) or any(keyword in description.lower() for keyword in keywords):
                with open(f'{repo_name_string}-issues.txt', 'a') as f:
                    f.write('\n------------------------------------------------------------------------------------------------------------------------------------------\n')
                    f.write(f'{title}: {issue["html_url"]}\n')
                    f.write(f'Description: {description}\n')
                    for comment in comments:
                        f.write(f'\t{comment["user"]["login"]}: {comment["body"]}\n')
        except:
            pass
