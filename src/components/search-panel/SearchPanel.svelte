<script lang="ts">
  import { onMount } from 'svelte';
  import { SearchPanel } from './SearchPanel';
  import type { Writable } from 'svelte/store';
  import type { SearchBarStoreValue } from '../../stores';
  import type { ClipLabel } from '../../types/common-types';
  import { config } from '../../config/config';
  import d3 from '../../utils/d3-import';
  import iconTop from '../../imgs/icon-top.svg?raw';
  import iconCancel from '../../imgs/icon-cancel.svg?raw';
  import iconSearch from '../../imgs/icon-search.svg?raw';
  import iconWizmap from '../../imgs/icon-wizmap.svg?raw';

  interface ClipItem {
    label: ClipLabel;
    name: string;
  }

  // export let searchPanelStore: Writable<SearchBarStoreValue>;

  // Components
  let component: HTMLElement | null = null;
  let mounted = false;
  let initialized = false;
  let mySearchPanel: SearchPanel | null = null;
  let searchInputValue = '';

  // Component states
  let inputFocused = false;
  const numberFormatter = d3.format(',');

  // Select all clips by default
  const allClipLabels: ClipLabel[] = [
    'no-comm',
    'one-way',
    'two-way',
    'runtime-data',
    'code-text',
    'external-data',
    'in-cell',
    'out-of-cell',
    'monolithic',
    'modular',
    'data-scientist',
    'scientist',
    'educator',
    'jupyter',
    'lab',
    'colab',
    'vscode',
    'ipywidget',
    'lab-extension',
    'html',
    'nova'
  ];
  let selectedClips = new Set<ClipLabel>(allClipLabels);

  const commClips: ClipItem[] = [
    { label: 'no-comm', name: 'No communication' },
    { label: 'one-way', name: 'One-way' },
    { label: 'two-way', name: 'Two-way' }
  ];

  const materialClips: ClipItem[] = [
    { label: 'runtime-data', name: 'Run-time data' },
    { label: 'code-text', name: 'Code and text' },
    { label: 'external-data', name: 'External Data' }
  ];

  const presentationClips: ClipItem[] = [
    { label: 'in-cell', name: 'In-cell' },
    { label: 'out-of-cell', name: 'Out-of-cell' }
  ];

  const modularityClips: ClipItem[] = [
    { label: 'monolithic', name: 'Monolithic' },
    { label: 'modular', name: 'Modular' }
  ];

  const userClips: ClipItem[] = [
    { label: 'data-scientist', name: 'Data Scientist' },
    { label: 'scientist', name: 'Scientist' },
    { label: 'educator', name: 'Educators and Students' }
  ];

  const notebookClips: ClipItem[] = [
    { label: 'jupyter', name: 'Jupyter Notebook' },
    { label: 'lab', name: 'JupyterLab' },
    { label: 'colab', name: 'Colab' },
    { label: 'vscode', name: 'VSCode Notebook' }
  ];

  const implementationClips: ClipItem[] = [
    { label: 'ipywidget', name: 'ipywidget' },
    { label: 'lab-extension', name: 'Lab extension' },
    { label: 'html', name: 'HTML display' },
    { label: 'nova', name: 'NOVA' }
  ];

  const searchPanelUpdated = () => {
    mySearchPanel = mySearchPanel;
  };

  /**
   * Handler for clip clicking event
   * @param clipLabel Clip label string
   */
  const clipClicked = (clipLabel: ClipLabel) => {
    if (selectedClips.has(clipLabel)) {
      selectedClips.delete(clipLabel);
    } else {
      selectedClips.add(clipLabel);
    }
    selectedClips = selectedClips;
  };

  onMount(() => {
    mounted = true;
  });

  /**
   * Initialize the embedding view.
   */
  const initView = () => {
    initialized = true;

    if (component) {
      mySearchPanel = new SearchPanel(component, searchPanelUpdated);
    }
  };

  $: mounted && !initialized && component && initView();
</script>

<style lang="scss">
  @import './SearchPanel.scss';
</style>

<div class="search-panel-wrapper" bind:this="{component}">
  <div class="search-bar" class:focused="{inputFocused}">
    <input
      type="text"
      id="search-bar-input"
      name="search-query"
      bind:value="{searchInputValue}"
      placeholder="Search notebook vis tools"
      spellcheck="false"
      on:focus="{() => {
        inputFocused = true;
      }}"
      on:blur="{() => {
        inputFocused = false;
      }}"
      on:input="{e => mySearchPanel?.inputChanged(e)}"
    />

    <div class="end-button">
      <div
        class="svg-icon search-icon"
        class:hidden="{searchInputValue.length !== 0}"
      >
        {@html iconSearch}
      </div>

      <button
        class="svg-icon cancel-icon"
        class:hidden="{searchInputValue.length === 0}"
        on:click="{() => {
          searchInputValue = '';
          mySearchPanel?.cancelSearch();
        }}"
      >
        {@html iconCancel}
      </button>
    </div>
  </div>

  <div class="category-block">
    <div class="name">Notebook Communication</div>
    <div class="chips-container">
      {#each commClips as clip, i}
        <button
          class="chip"
          on:click="{() => clipClicked(clip.label)}"
          class:selected="{selectedClips.has(clip.label)}">{clip.name}</button
        >
      {/each}
    </div>
  </div>

  <div class="category-block">
    <div class="name">Visualization Material</div>
    <div class="chips-container">
      {#each materialClips as clip, i}
        <button
          class="chip"
          on:click="{() => clipClicked(clip.label)}"
          class:selected="{selectedClips.has(clip.label)}">{clip.name}</button
        >
      {/each}
    </div>
  </div>

  <div class="category-block">
    <div class="name">Visualization Presentation</div>
    <div class="chips-container">
      {#each presentationClips as clip, i}
        <button
          class="chip"
          on:click="{() => clipClicked(clip.label)}"
          class:selected="{selectedClips.has(clip.label)}">{clip.name}</button
        >
      {/each}
    </div>
  </div>

  <div class="category-block">
    <div class="name">Modularity</div>
    <div class="chips-container">
      {#each modularityClips as clip, i}
        <button
          class="chip"
          on:click="{() => clipClicked(clip.label)}"
          class:selected="{selectedClips.has(clip.label)}">{clip.name}</button
        >
      {/each}
    </div>
  </div>

  <div class="category-block">
    <div class="name">Targeted Users</div>
    <div class="chips-container">
      {#each userClips as clip, i}
        <button
          class="chip"
          on:click="{() => clipClicked(clip.label)}"
          class:selected="{selectedClips.has(clip.label)}">{clip.name}</button
        >
      {/each}
    </div>
  </div>

  <div class="category-block">
    <div class="name">Supported Notebooks</div>
    <div class="chips-container">
      {#each notebookClips as clip, i}
        <button
          class="chip"
          on:click="{() => clipClicked(clip.label)}"
          class:selected="{selectedClips.has(clip.label)}">{clip.name}</button
        >
      {/each}
    </div>
  </div>

  <div class="category-block">
    <div class="name">Implementation Method</div>
    <div class="chips-container">
      {#each implementationClips as clip, i}
        <button
          class="chip"
          on:click="{() => clipClicked(clip.label)}"
          class:selected="{selectedClips.has(clip.label)}">{clip.name}</button
        >
      {/each}
    </div>
  </div>
</div>
