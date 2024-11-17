'use client';

import React from "react";

import { Theme } from "@gravity-ui/uikit";
import { DEFAULT_THEME, ThemeContext } from "./ThemeContext";

export const ThemeContextProvider = ({ children }: { children: React.ReactNode }) => {
    const [theme, setTheme] = React.useState<Theme>(DEFAULT_THEME);

    return (
        <ThemeContext.Provider value={{ theme, setTheme }}>
            {children}
        </ThemeContext.Provider>
    );
};
