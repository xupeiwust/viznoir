import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
  spring,
  useVideoConfig,
} from "remotion";
import { colors, fonts, fullScreen } from "../styles";

interface StatCardProps {
  value: string;
  label: string;
  color: string;
  delay: number;
}

const StatCard: React.FC<StatCardProps> = ({ value, label, color, delay }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const scale = spring({
    frame: frame - delay,
    fps,
    from: 0,
    to: 1,
    durationInFrames: 25,
  });

  const opacity = interpolate(frame, [delay, delay + 15], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Count-up animation for numbers
  const numericValue = parseInt(value.replace(/\D/g, ""), 10);
  const suffix = value.replace(/\d/g, "");
  const countFrame = Math.max(0, frame - delay - 10);
  const displayNum = Math.min(
    Math.floor(interpolate(countFrame, [0, 40], [0, numericValue], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })),
    numericValue
  );

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 12,
        opacity,
        transform: `scale(${scale})`,
      }}
    >
      <div
        style={{
          fontSize: 96,
          fontWeight: 800,
          color,
          fontFamily: fonts.sans,
          lineHeight: 1,
        }}
      >
        {displayNum}
        {suffix}
      </div>
      <div
        style={{
          fontSize: 28,
          color: colors.gray,
          fontFamily: fonts.sans,
        }}
      >
        {label}
      </div>
    </div>
  );
};

const clients = ["Claude Code", "Cursor", "Gemini CLI", "Codex CLI"];

export const SceneFeatures: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Clients section appears after stats
  const clientsOpacity = interpolate(frame, [200, 230], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const clientsY = spring({
    frame: frame - 200,
    fps,
    from: 40,
    to: 0,
    durationInFrames: 30,
  });

  return (
    <AbsoluteFill style={fullScreen}>
      {/* Stats row */}
      <div
        style={{
          display: "flex",
          gap: 120,
          marginBottom: 100,
        }}
      >
        <StatCard value="13" label="MCP Tools" color={colors.accent} delay={10} />
        <StatCard value="331" label="Tests Passing" color={colors.green} delay={40} />
        <StatCard value="50+" label="File Formats" color="#a78bfa" delay={70} />
      </div>

      {/* Supported clients */}
      <div
        style={{
          opacity: clientsOpacity,
          transform: `translateY(${clientsY}px)`,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 24,
        }}
      >
        <div
          style={{
            fontSize: 24,
            color: colors.dim,
            fontFamily: fonts.sans,
            textTransform: "uppercase",
            letterSpacing: 4,
          }}
        >
          Works with
        </div>
        <div style={{ display: "flex", gap: 40 }}>
          {clients.map((client, i) => {
            const pillOpacity = interpolate(
              frame,
              [220 + i * 15, 235 + i * 15],
              [0, 1],
              { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
            );
            return (
              <div
                key={client}
                style={{
                  padding: "12px 28px",
                  borderRadius: 999,
                  backgroundColor: colors.bgLight,
                  border: `1px solid ${colors.dim}`,
                  color: colors.white,
                  fontSize: 22,
                  fontFamily: fonts.sans,
                  fontWeight: 500,
                  opacity: pillOpacity,
                }}
              >
                {client}
              </div>
            );
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};
