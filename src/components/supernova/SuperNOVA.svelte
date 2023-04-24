<script lang="ts">
  import logoDiffusionDB from '../../imgs/logo-diffusiondb.svg?raw';
  import iconGithub from '../../imgs/icon-github.svg?raw';

  let component: HTMLElement | null = null;
</script>

<style lang="scss">
  @import './supernova.scss';
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

  <div class="app-wrapper">
    <div class="main-app" bind:this={component}>
      <div class="main-app-container">Hello</div>
    </div>
  </div>

  <div class="footer-container">Footer</div>

  <div class="search-panel-container">Search</div>
</div>
