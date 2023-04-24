<script lang="ts">
  import { onMount } from 'svelte';
  import { SearchPanel } from './SearchPanel';
  import type { Writable } from 'svelte/store';
  import type { SearchBarStoreValue } from '../../stores';
  import { config } from '../../config/config';
  import d3 from '../../utils/d3-import';
  import iconTop from '../../imgs/icon-top.svg?raw';
  import iconCancel from '../../imgs/icon-cancel.svg?raw';
  import iconSearch from '../../imgs/icon-search.svg?raw';
  import iconWizmap from '../../imgs/icon-wizmap.svg?raw';

  export let searchPanelStore: Writable<SearchBarStoreValue>;

  // Components
  let component: HTMLElement | null = null;
  let mounted = false;
  let initialized = false;
  let mySearchPanel: SearchPanel | null = null;
  let resultListElement: HTMLElement | null = null;
  let searchInputValue = '';

  // Component states
  let inputFocused = false;
  let searchScrolled = false;
  let showScrollTopButton = false;

  let maxListLength = 100;
  const numberFormatter = d3.format(',');

  const searchPanelUpdated = () => {
    mySearchPanel = mySearchPanel;
  };

  onMount(() => {
    mounted = true;
  });

  /**
   * Initialize the embedding view.
   */
  const initView = () => {
    initialized = true;

    if (component && searchPanelStore) {
      mySearchPanel = new SearchPanel(component, searchPanelUpdated);
    }
  };

  $: mounted && !initialized && component && initView();
</script>

<style lang="scss">
  @import './SearchPanel.scss';
</style>

<div class="search-panel-wrapper" bind:this={component}>
  <div class="search-bar" class:focused={inputFocused}>
    <input
      type="text"
      id="search-bar-input"
      name="search-query"
      bind:value={searchInputValue}
      placeholder="Search notebook vis tools"
      spellcheck="false"
      on:focus={() => {
        inputFocused = true;
      }}
      on:blur={() => {
        inputFocused = false;
      }}
      on:input={(e) => mySearchPanel?.inputChanged(e)}
    />

    <div class="end-button">
      <div
        class="svg-icon search-icon"
        class:hidden={searchInputValue.length !== 0}
      >
        {@html iconSearch}
      </div>

      <button
        class="svg-icon cancel-icon"
        class:hidden={searchInputValue.length === 0}
        on:click={() => {
          searchInputValue = '';
          mySearchPanel?.cancelSearch();
        }}
      >
        {@html iconCancel}
      </button>
    </div>
  </div>
</div>
