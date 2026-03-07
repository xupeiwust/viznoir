import { CSSProperties } from "react";

export const colors = {
  bg: "#0f172a",
  bgLight: "#1e293b",
  accent: "#3b82f6",
  green: "#10b981",
  red: "#ef4444",
  white: "#f8fafc",
  gray: "#94a3b8",
  dim: "#64748b",
};

export const fonts = {
  sans: "Inter, system-ui, sans-serif",
  mono: "'JetBrains Mono', 'Fira Code', monospace",
};

export const fullScreen: CSSProperties = {
  width: "100%",
  height: "100%",
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  justifyContent: "center",
  backgroundColor: colors.bg,
  fontFamily: fonts.sans,
  color: colors.white,
};

export const terminalBox: CSSProperties = {
  backgroundColor: "#0d1117",
  borderRadius: 16,
  padding: "32px 40px",
  fontFamily: fonts.mono,
  fontSize: 28,
  lineHeight: 1.8,
  border: `1px solid ${colors.dim}`,
  minWidth: 900,
};
