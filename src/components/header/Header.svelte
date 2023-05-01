<script lang="ts">
  let component: HTMLElement | null = null;
</script>

<style lang="scss">
  @import './Header.scss';
</style>

<div class="header-wrapper" bind:this="{component}">
  <div class="header-content">
    <div class="left-content">
      <div class="app-title">SuperNOVA</div>
      <div class="app-tagline">
        A Collection of 150 Interactive Visualization Tools for Computational
        Notebooks
      </div>
    </div>

    <div class="right-content">
      <a class="right-button" href="https://github.com/poloclub/supernova"
        >Code</a
      >
      <a class="right-button" href="https://github.com/poloclub/supernova"
        >Paper</a
      >
      <a
        class="right-button"
        href="https://github.com/poloclub/supernova#how-to-add-an-entry-to-supernova"
        >Add New Tool</a
      >
    </div>
  </div>
</div>
