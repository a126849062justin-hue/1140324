module.exports = {
  content: ["./*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Noto Sans TC"', 'sans-serif'],
        serif: ['"Cormorant Garamond"', 'serif'],
      },
      colors: {
        brand: {
          bg: 'rgb(var(--color-bg) / <alpha-value>)',
          panel: 'rgb(var(--color-panel) / <alpha-value>)',
          text: 'rgb(var(--color-text) / <alpha-value>)',
          border: 'rgb(var(--color-border) / <alpha-value>)',
          muted: 'rgb(var(--color-muted) / <alpha-value>)',
          red: 'rgb(var(--color-red) / <alpha-value>)',
          redDark: 'rgb(var(--color-red-dark) / <alpha-value>)'
        }
      }
    }
  }
}
