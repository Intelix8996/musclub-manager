import type { Metadata } from 'next';

import '@gravity-ui/uikit/styles/fonts.css';
import '@gravity-ui/uikit/styles/styles.css';

import '../styles/globals.scss';

import { ThemeContextProvider } from '@/components/theme/ThemeContext/ThemeContextProvider';
import { ThemeProvider } from '@/components/theme/ThemeProvider/ThemeProvider';
import { Layout } from '@/components/Layout/Layout';
import { DEFAULT_THEME } from '@/components/theme/ThemeContext/ThemeContext';

export const metadata: Metadata = {
    title: 'Musclub Manager',
    description: 'Website for managing events and staff',
};

const DEFAULT_BODY_CLASSNAME = `g-root g-root_theme_${DEFAULT_THEME}`;

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="en">
            <body className={DEFAULT_BODY_CLASSNAME}>
                <ThemeContextProvider>
                    <ThemeProvider>
                        <Layout>
                            {children}
                        </Layout>
                    </ThemeProvider>
                </ThemeContextProvider>
            </body>
        </html>
    );
}
