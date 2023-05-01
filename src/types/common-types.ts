/**
 * Common types.
 */

export interface SuperNovaEntry {
  name: string;
  nameDisplay: string;
  githubURL: string;
  paperURL: string;
  otherURLs: string[];
  description: string;
  bibtex: string;
  bibtexKey: string;
  sourceType: SourceString;
  releaseYear: number;
  communication: CommunicationString;
  materials: MaterialString[];
  layouts: layoutString[];
  supportedNotebooks: NotebookString[];
  modularity: ModularityString;
  user: UserString;
  implementation: ImplementationString;
  allClips: Set<ClipLabel>;
}

type SourceString = 'paper' | 'package';
type CommunicationString = 'no' | 'one-way' | 'two-way';
type MaterialString = 'runtime' | 'code' | 'external';
type layoutString = 'demand' | 'always';
type ModularityString = 'mono' | 'modular';
type UserString = 'data scientist' | 'scientist' | 'educator';
type NotebookString = 'jupyter' | 'lab' | 'colab' | 'vscode';
type ImplementationString =
  | 'ipywidget'
  | 'extension'
  | 'html'
  | 'nova'
  | 'custom';

export type ClipLabel =
  | CommunicationString
  | MaterialString
  | layoutString
  | ModularityString
  | UserString
  | NotebookString
  | ImplementationString;

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
