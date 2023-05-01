import { writable } from 'svelte/store';
import type { ClipLabel } from './types/common-types';

export interface SearchStoreValue {
  selectedClips: Set<ClipLabel>;
  keyword: string;
}

export const getSearchStoreDefaultValue = (): SearchStoreValue => {
  return {
    selectedClips: new Set(),
    keyword: ''
  };
};

export const getSearchStore = () => {
  return writable(getSearchStoreDefaultValue());
};
