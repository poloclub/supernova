<script lang="ts">
  import { onMount } from 'svelte';
  import type { Writable } from 'svelte/store';
  import { GridPanel } from './GridPanel';
  import { config } from '../../config/config';
  import type { ClipLabel } from '../../types/common-types';
  import type { SuperNovaEntry } from '../../types/common-types';
  import type { SearchStoreValue } from '../../stores';
  import { getSearchStoreDefaultValue } from '../../stores';
  import d3 from '../../utils/d3-import';
  import iconCancel from '../../imgs/icon-cancel.svg?raw';
  import iconFile from '../../imgs/icon-file.svg?raw';
  import iconGithub from '../../imgs/icon-github.svg?raw';
  import iconHome from '../../imgs/icon-home.svg?raw';
  import supernova from '../../data/supernova.yaml';

  interface ClipItem {
    label: ClipLabel;
    name: string;
  }

  export let searchStore: Writable<SearchStoreValue>;

  // Components
  let component: HTMLElement | null = null;
  let mounted = false;
  let initialized = false;
  let myGridPanel: GridPanel | null = null;
  let dialogElement: HTMLDialogElement | null = null;
  let showingEntry: SuperNovaEntry | null = null;

  const supernovaEntries = supernova as SuperNovaEntry[];

  const getAllClips = (entry: SuperNovaEntry) => {
    const curClips: ClipLabel[] = [];
    curClips.push(entry.user);
    curClips.push(entry.communication);
    entry.materials.forEach(d => curClips.push(d));
    entry.layouts.forEach(d => curClips.push(d));
    entry.supportedNotebooks.forEach(d => curClips.push(d));
    curClips.push(entry.implementation);
    return new Set(curClips);
  };

  for (const entry of supernovaEntries) {
    entry.allClips = getAllClips(entry);
  }

  const allClipItems: ClipItem[] = [
    { label: 'no', name: 'No communication' },
    { label: 'one-way', name: 'One-way' },
    { label: 'two-way', name: 'Two-way' },
    { label: 'runtime', name: 'Run-time data' },
    { label: 'code', name: 'Code and text' },
    { label: 'external', name: 'External Data' },
    { label: 'on-demand', name: 'In-cell' },
    { label: 'always-on', name: 'Out-of-cell' },
    { label: 'mono', name: 'Monolithic' },
    { label: 'modular', name: 'Modular' },
    { label: 'data scientist', name: 'Data Scientist' },
    { label: 'scientist', name: 'Scientist' },
    { label: 'educator', name: 'Educators and Students' },
    { label: 'jupyter', name: 'Jupyter Notebook' },
    { label: 'lab', name: 'JupyterLab' },
    { label: 'colab', name: 'Colab' },
    { label: 'vscode', name: 'VSCode Notebook' },
    { label: 'ipywidget', name: 'ipywidget' },
    { label: 'extension', name: 'Lab extension' },
    { label: 'html', name: 'HTML display' },
    { label: 'nova', name: 'NOVA' }
  ];

  const numberFormatter = d3.format(',');

  const gridPanelUpdated = () => {
    myGridPanel = myGridPanel;
  };

  onMount(() => {
    mounted = true;

    console.log(supernova);
  });

  /**
   * Initialize the embedding view.
   */
  const initView = () => {
    initialized = true;

    if (component) {
      myGridPanel = new GridPanel(
        component,
        gridPanelUpdated,
        supernovaEntries,
        searchStore
      );
    }
  };

  $: mounted && !initialized && component && initView();
</script>

<style lang="scss">
  @import './GridPanel.scss';
</style>

<div class="grid-panel-wrapper" bind:this="{component}">
  <dialog id="image-dialog" bind:this="{dialogElement}">
    {#if showingEntry !== null}
      <div class="header">
        <div class="left">
          <span class="header-title">
            {`${showingEntry.nameDisplay} (${showingEntry.releaseYear})`}
          </span>

          {#if showingEntry.githubURL !== ''}
            <a href="{showingEntry.githubURL}" target="_blank">
              <span class="svg-icon">
                {@html iconGithub}
              </span>
            </a>
          {/if}

          {#if showingEntry.paperURL !== ''}
            <a href="{showingEntry.paperURL}" target="_blank">
              <span class="svg-icon">
                {@html iconFile}
              </span>
            </a>
          {/if}

          {#each showingEntry.otherURLs as url}
            <a href="{url}" target="_blank">
              <span class="svg-icon">
                {@html iconHome}
              </span>
            </a>
          {/each}
        </div>
        <div class="right">
          <button
            class="close-button"
            on:click="{() => {
              dialogElement?.close();
            }}"
          >
            <div class="svg-icon no-pointer">
              {@html iconCancel}
            </div>
          </button>
        </div>
      </div>

      <div class="content">
        <div class="description">{showingEntry.description}</div>

        <div class="thumbnail-container">
          <img
            class="thumbnail"
            src="{`${import.meta.env.BASE_URL}images/thumbnails/${
              showingEntry?.name
            }.webp`}"
            alt="{`Thumbnail of ${showingEntry.name}`}"
          />
        </div>
      </div>

      <div class="info-bar">
        {#each allClipItems as clipItem}
          {#if showingEntry.allClips.has(clipItem.label)}
            <div class="clip">{clipItem.name}</div>
          {/if}
        {/each}
      </div>
    {/if}
  </dialog>

  <div class="content-wrapper">
    <div class="row-header">
      <span class="label"
        >{`Showing ${myGridPanel ? myGridPanel.curEntries.length : 0} / ${
          supernovaEntries.length
        } visual analytics tools, sorted by`}
      </span>
      <span class="label">
        <div class="select" id="hidden-select">
          <select>
            <option id="hidden-option"></option>
          </select>
        </div>
        <div class="select">
          <select
            id="sort-select"
            on:change="{e => myGridPanel?.sortSelectChanged(e)}"
          >
            <!-- <option value="star-">star counts (↓)</option>
            <option value="star+">star counts (↑)</option> -->
            <option value="date-">release dates (↓)</option>
            <option value="date+">release dates (↑)</option>
            <option value="name+">name (A-Z)</option>
            <option value="name-">name (Z–A)</option>
          </select>
        </div>
      </span>
    </div>

    <div class="card-panel">
      {#if myGridPanel !== null}
        {#each myGridPanel.curEntries as entry}
          <div
            class="card"
            on:click="{() => {
              showingEntry = entry;
              dialogElement?.showModal();
            }}"
          >
            <img
              class="thumbnail"
              src="{`${import.meta.env.BASE_URL}images/thumbnails/${
                entry.name
              }.webp`}"
              alt="{`Thumbnail of ${entry.name}`}"
            />

            <div class="name">
              {entry.name}
            </div>
          </div>
        {/each}
      {/if}
    </div>
  </div>
</div>
