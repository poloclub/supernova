import type { Writable } from 'svelte/store';
import type { SearchStoreValue } from '../../stores';
import { getSearchStoreDefaultValue } from '../../stores';
import type { SuperNovaEntry } from '../../types/common-types';
import { setIntersect } from '../../utils/utils';

export class GridPanel {
  component: HTMLElement;
  gridPanelUpdated: () => void;
  allEntries: SuperNovaEntry[];
  curEntries: SuperNovaEntry[];
  searchStore: Writable<SearchStoreValue>;
  searchStoreValue = getSearchStoreDefaultValue();

  constructor(
    component: HTMLElement,
    gridPanelUpdated: () => void,
    supernovaEntries: SuperNovaEntry[],
    searchStore: Writable<SearchStoreValue>
  ) {
    this.component = component;
    this.gridPanelUpdated = gridPanelUpdated;
    this.allEntries = supernovaEntries.map(d => d);
    this.curEntries = supernovaEntries.map(d => d);
    this.searchStore = searchStore;

    this.searchStore.subscribe(value => {
      this.searchStoreValue = value;

      this.filterEntries();
    });

    // Default sorting is date-
    this.sortEntries('date-');
  }

  filterEntries = () => {
    // Check the selected clips
    this.curEntries = [];

    for (const entry of this.allEntries) {
      let addCurEntry = true;

      // Add this item if none of its clip is out of selection
      for (const clip of entry.allClips) {
        if (!this.searchStoreValue.selectedClips.has(clip)) {
          addCurEntry = false;
          break;
        }
      }

      // Check the search keyword
      if (this.searchStoreValue.keyword !== '') {
        const keyword = this.searchStoreValue.keyword.toLowerCase();
        const entryString = JSON.stringify(entry).toLowerCase();
        if (!entryString.includes(keyword)) {
          addCurEntry = false;
        }
      }

      if (addCurEntry) {
        this.curEntries.push(entry);
      }
    }

    this.gridPanelUpdated();
  };

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

        this.allEntries.sort((a, b) => a.name.localeCompare(b.name));
        this.allEntries.sort((a, b) => a.releaseYear - b.releaseYear);
        this.gridPanelUpdated();
        break;
      }

      case 'date-': {
        // Use name to break ties
        this.curEntries.sort((a, b) => a.name.localeCompare(b.name));
        this.curEntries.sort((a, b) => b.releaseYear - a.releaseYear);

        this.allEntries.sort((a, b) => a.name.localeCompare(b.name));
        this.allEntries.sort((a, b) => b.releaseYear - a.releaseYear);
        this.gridPanelUpdated();
        break;
      }

      case 'name+': {
        // Use year to break ties
        this.curEntries.sort((a, b) => b.releaseYear - a.releaseYear);
        this.curEntries.sort((a, b) => a.name.localeCompare(b.name));

        this.allEntries.sort((a, b) => b.releaseYear - a.releaseYear);
        this.allEntries.sort((a, b) => a.name.localeCompare(b.name));
        this.gridPanelUpdated();
        break;
      }

      case 'name-': {
        // Use yar to break ties
        this.curEntries.sort((a, b) => b.releaseYear - a.releaseYear);
        this.curEntries.sort((a, b) => b.name.localeCompare(a.name));

        this.allEntries.sort((a, b) => b.releaseYear - a.releaseYear);
        this.allEntries.sort((a, b) => b.name.localeCompare(a.name));
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
