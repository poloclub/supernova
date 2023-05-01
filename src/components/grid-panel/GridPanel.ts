import type { Writable } from 'svelte/store';
import d3 from '../../utils/d3-import';
import type { SearchBarStoreValue } from '../../stores';
import { getSearchBarStoreDefaultValue } from '../../stores';
import type { SuperNovaEntry } from '../../types/common-types';

export class GridPanel {
  component: HTMLElement;
  gridPanelUpdated: () => void;
  curEntries: SuperNovaEntry[];

  constructor(
    component: HTMLElement,
    gridPanelUpdated: () => void,
    supernovaEntries: SuperNovaEntry[]
  ) {
    this.component = component;
    this.gridPanelUpdated = gridPanelUpdated;
    this.curEntries = supernovaEntries.map(d => d);

    // Default sorting is date-
    this.sortEntries('date-');
  }

  /**
   * Event handler for the sorting key selection chagne
   * @param e Select input event
   */
  sortSelectChanged = (e: InputEvent) => {
    const target = e.target as HTMLInputElement;
    const sortKey = target.value;

    if (
      sortKey === 'date+' ||
      sortKey === 'date-' ||
      sortKey === 'name+' ||
      sortKey === 'name-'
    ) {
      this.sortEntries(sortKey);
    }
  };

  sortEntries = (key: 'date+' | 'date-' | 'name+' | 'name-') => {
    switch (key) {
      case 'date+': {
        // Use name to break ties
        this.curEntries.sort((a, b) => a.name.localeCompare(b.name));
        this.curEntries.sort((a, b) => a.releaseYear - b.releaseYear);
        this.gridPanelUpdated();
        break;
      }

      case 'date-': {
        // Use name to break ties
        this.curEntries.sort((a, b) => a.name.localeCompare(b.name));
        this.curEntries.sort((a, b) => b.releaseYear - a.releaseYear);
        this.gridPanelUpdated();
        break;
      }

      case 'name+': {
        // Use year to break ties
        this.curEntries.sort((a, b) => b.releaseYear - a.releaseYear);
        this.curEntries.sort((a, b) => a.name.localeCompare(b.name));
        this.gridPanelUpdated();
        break;
      }

      case 'name-': {
        // Use yar to break ties
        this.curEntries.sort((a, b) => b.releaseYear - a.releaseYear);
        this.curEntries.sort((a, b) => b.name.localeCompare(a.name));
        this.gridPanelUpdated();
        break;
      }

      default: {
        console.error('Unknown sorting key', key);
        break;
      }
    }
  };
}
