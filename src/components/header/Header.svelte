<script lang="ts">
  let component: HTMLElement | null = null;
  import iconSupernova from '../../imgs/supernova-logo.svg?raw';
</script>

<style lang="scss">
  @import './Header.scss';
</style>

<div class="header-wrapper" bind:this="{component}">
  <div class="header-content">
    <div class="left-content">
      <div class="app-title">
        <svg class="svg-icon">
          {@html iconSupernova}
        </svg>
      </div>
      <div class="app-tagline">
        A Collection of 150 Interactive Visualization Tools for Computational
        Notebooks
      </div>
    </div>

    <div class="right-content">
      <a class="right-button" href="https://github.com/poloclub/supernova"
        >Code</a
      >
      <a class="right-button" href="http://arxiv.org/abs/2305.03039">Paper</a>
      <a
        class="right-button"
        href="https://github.com/poloclub/supernova#how-to-add-an-entry-to-supernova"
        >Add New Tool</a
      >
    </div>
  </div>
</div>
