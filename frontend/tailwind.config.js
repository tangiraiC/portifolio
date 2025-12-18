/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                'cosmic-bg': '#0a0a16',
                'cosmic-card': '#1a1a2e',
                'cosmic-accent': '#7b2cbf',
                'cosmic-text': '#e0e0e0',
            },
        },
    },
    plugins: [],
}
