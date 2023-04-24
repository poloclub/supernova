/**
 * Common types.
 */

export type ClipLabel =
  | 'no-comm'
  | 'one-way'
  | 'two-way'
  | 'runtime-data'
  | 'code-text'
  | 'external-data'
  | 'in-cell'
  | 'out-of-cell'
  | 'monolithic'
  | 'modular'
  | 'data-scientist'
  | 'scientist'
  | 'educator'
  | 'jupyter'
  | 'lab'
  | 'colab'
  | 'vscode'
  | 'ipywidget'
  | 'lab-extension'
  | 'html'
  | 'nova';

export interface Padding {
  top: number;
  bottom: number;
  left: number;
  right: number;
}

export interface Rect {
  x: number;
  y: number;
  width: number;
  height: number;
}

export interface Point {
  x: number;
  y: number;
}

export interface Size {
  width: number;
  height: number;
}
