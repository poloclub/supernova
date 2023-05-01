import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import yaml from '@rollup/plugin-yaml';

// // https://vitejs.dev/config/
// export default defineConfig({
//   plugins: [svelte()]
// });

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {
  if (command === 'serve') {
    // Development
    return {
      plugins: [yaml(), svelte()]
    };
  } else if (command === 'build') {
    switch (mode) {
      case 'production': {
        // Production: standard web page (default mode)
        return {
          build: {
            outDir: 'dist'
          },
          plugins: [yaml(), svelte()]
        };
      }

      case 'vercel': {
        // Production: for vercel demo
        return {
          build: {
            outDir: 'dist'
          },
          plugins: [yaml(), svelte()]
        };
      }

      case 'github': {
        // Production: github page
        return {
          base: '/supernova/',
          build: {
            outDir: 'gh-page'
          },
          plugins: [yaml(), svelte()]
        };
      }

      default: {
        console.error(`Unknown production mode ${mode}`);
        return null;
      }
    }
  }
});
