'use client';

import React from "react";

import { ThemeProvider as GravityUiThemeProvider } from "@gravity-ui/uikit";
import { ThemeContext } from "../ThemeContext/ThemeContext";


export const ThemeProvider = ({ children }: { children: React.ReactNode }) => {
    const { theme } = React.useContext(ThemeContext);

    return (
        <GravityUiThemeProvider theme={theme}>
            {children}
        </GravityUiThemeProvider>
    );
}
