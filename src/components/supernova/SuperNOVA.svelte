<script lang="ts">
  import Header from '../header/Header.svelte';
  import iconGithub from '../../imgs/icon-github.svg?raw';

  let component: HTMLElement | null = null;
</script>

<style lang="scss">
  @import './SuperNOVA.scss';
</style>

<div class="supernova-page">
  <div id="popper-tooltip-top" class="popper-tooltip hidden" role="tooltip">
    <span class="popper-content" />
    <div class="popper-arrow" />
  </div>

  <div id="popper-tooltip-bottom" class="popper-tooltip hidden" role="tooltip">
    <span class="popper-content" />
    <div class="popper-arrow" />
  </div>

  <div class="main-app" bind:this={component}>
    <div class="header-container">
      <Header />
    </div>

    <div class="content-container">
      <div class="search-container">Search</div>

      <div class="card-container">Card</div>
    </div>
  </div>
</div>
