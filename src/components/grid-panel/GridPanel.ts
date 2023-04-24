import type { Writable } from 'svelte/store';
import d3 from '../../utils/d3-import';
import type { SearchBarStoreValue } from '../../stores';
import { getSearchBarStoreDefaultValue } from '../../stores';

export class GridPanel {
  component: HTMLElement;
  gridPanelUpdated: () => void;

  constructor(component: HTMLElement, gridPanelUpdated: () => void) {
    this.component = component;
    this.gridPanelUpdated = gridPanelUpdated;
  }
}
