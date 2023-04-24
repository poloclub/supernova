<script lang="ts">
  let component: HTMLElement | null = null;
</script>

<style lang="scss">
  @import './Header.scss';
</style>

<div class="header-wrapper" bind:this={component}>
  <div class="left-content">
    <div class="app-title">SuperNOVA</div>
    <div class="app-tagline">
      A Collection of 150 Interactive Visualization Tools for Computational
      Notebooks
    </div>
  </div>

  <div class="right-content">
    <div class="right-button">Code</div>
    <div class="right-button">Paper</div>
    <div class="right-button">Add Tool</div>
  </div>
</div>
