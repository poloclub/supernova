<script lang="ts">
  import Header from '../header/Header.svelte';
  import SearchPanel from '../search-panel/SearchPanel.svelte';
  import GridPanel from '../grid-panel/GridPanel.svelte';
  import iconGithub from '../../imgs/icon-github.svg?raw';
  import { getSearchStore } from '../../stores';

  let component: HTMLElement | null = null;
  const searchStore = getSearchStore();
</script>

<style lang="scss">
  @import './SuperNOVA.scss';
</style>

<div class="supernova-page">
  <div id="popper-tooltip-top" class="popper-tooltip hidden" role="tooltip">
    <span class="popper-content"></span>
    <div class="popper-arrow"></div>
  </div>

  <div id="popper-tooltip-bottom" class="popper-tooltip hidden" role="tooltip">
    <span class="popper-content"></span>
    <div class="popper-arrow"></div>
  </div>

  <div class="main-app" bind:this="{component}">
    <div class="header-container">
      <Header />
    </div>

    <div class="search-container">
      <SearchPanel searchStore="{searchStore}" />
    </div>

    <div class="card-container">
      <GridPanel searchStore="{searchStore}" />
    </div>
  </div>
</div>
