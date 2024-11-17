'use client';

import React from "react";
import { SetStateAction } from "react";

import { Theme } from "@gravity-ui/uikit";

export const DARK_THEME = 'dark';
export const LIGHT_THEME = 'light';
export const DEFAULT_THEME = DARK_THEME;

type ThemeContextProps = {
    theme: Theme,
    setTheme: React.Dispatch<SetStateAction<Theme>>,
}

export const ThemeContext = React.createContext<ThemeContextProps>({ theme: DEFAULT_THEME, setTheme: () => { } });
