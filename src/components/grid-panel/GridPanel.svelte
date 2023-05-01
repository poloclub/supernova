<script lang="ts">
  import { onMount } from 'svelte';
  import { GridPanel } from './GridPanel';
  import { config } from '../../config/config';
  import type { SuperNovaEntry } from '../../types/common-types';
  import d3 from '../../utils/d3-import';
  import iconCancel from '../../imgs/icon-cancel.svg?raw';
  import iconSearch from '../../imgs/icon-search.svg?raw';
  import supernova from '../../data/supernova.yaml';

  // Components
  let component: HTMLElement | null = null;
  let mounted = false;
  let initialized = false;
  let myGridPanel: GridPanel | null = null;

  const supernovaEntries = supernova as SuperNovaEntry[];

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
        supernovaEntries
      );
    }
  };

  $: mounted && !initialized && component && initView();
</script>

<style lang="scss">
  @import './GridPanel.scss';
</style>

<div class="grid-panel-wrapper" bind:this="{component}">
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
          <div class="card">
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
