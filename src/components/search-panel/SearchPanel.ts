import type { Writable } from 'svelte/store';
import d3 from '../../utils/d3-import';
import type { SearchBarStoreValue } from '../../stores';
import { getSearchBarStoreDefaultValue } from '../../stores';

export class SearchPanel {
  component: HTMLElement;
  SearchPanelUpdated: () => void;

  constructor(component: HTMLElement, SearchPanelUpdated: () => void) {
    this.component = component;
    this.SearchPanelUpdated = SearchPanelUpdated;
  }
}
