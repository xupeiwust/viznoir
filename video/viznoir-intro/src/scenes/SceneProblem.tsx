import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
  spring,
  useVideoConfig,
} from "remotion";
import { colors, fonts, fullScreen } from "../styles";

export const SceneProblem: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleOpacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: "clamp",
  });

  const titleY = spring({ frame, fps, from: 40, to: 0, durationInFrames: 30 });

  const crossScale = spring({
    frame: frame - 40,
    fps,
    from: 0,
    to: 1,
    durationInFrames: 20,
  });

  const fadeOut = interpolate(frame, [120, 150], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ ...fullScreen, opacity: fadeOut }}>
      {/* Mock ParaView GUI */}
      <div
        style={{
          width: 800,
          height: 500,
          backgroundColor: "#2d2d2d",
          borderRadius: 12,
          border: `2px solid ${colors.dim}`,
          display: "flex",
          flexDirection: "column",
          overflow: "hidden",
          opacity: titleOpacity,
          transform: `translateY(${titleY}px)`,
        }}
      >
        {/* Title bar */}
        <div
          style={{
            height: 40,
            backgroundColor: "#3c3c3c",
            display: "flex",
            alignItems: "center",
            padding: "0 16px",
            gap: 8,
          }}
        >
          <div
            style={{
              width: 12,
              height: 12,
              borderRadius: "50%",
              backgroundColor: colors.red,
            }}
          />
          <div
            style={{
              width: 12,
              height: 12,
              borderRadius: "50%",
              backgroundColor: "#fbbf24",
            }}
          />
          <div
            style={{
              width: 12,
              height: 12,
              borderRadius: "50%",
              backgroundColor: colors.green,
            }}
          />
          <span
            style={{
              color: colors.gray,
              fontSize: 14,
              fontFamily: fonts.sans,
              marginLeft: 12,
            }}
          >
            ParaView 5.12 - Traditional GUI
          </span>
        </div>
        {/* GUI body with menus */}
        <div style={{ flex: 1, display: "flex" }}>
          <div
            style={{
              width: 200,
              backgroundColor: "#353535",
              borderRight: `1px solid ${colors.dim}`,
              padding: 12,
            }}
          >
            {["Pipeline Browser", "Properties", "Filters", "Sources"].map(
              (item) => (
                <div
                  key={item}
                  style={{
                    color: colors.gray,
                    fontSize: 13,
                    padding: "6px 0",
                    fontFamily: fonts.sans,
                  }}
                >
                  {item}
                </div>
              )
            )}
          </div>
          <div
            style={{
              flex: 1,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              backgroundColor: "#1a1a1a",
            }}
          >
            <span
              style={{ color: colors.dim, fontSize: 16, fontFamily: fonts.sans }}
            >
              [3D Viewport - Click, Drag, Menu, Repeat...]
            </span>
          </div>
        </div>
      </div>

      {/* Red X overlay */}
      <div
        style={{
          position: "absolute",
          transform: `scale(${crossScale})`,
        }}
      >
        <svg width="200" height="200" viewBox="0 0 200 200">
          <line
            x1="40"
            y1="40"
            x2="160"
            y2="160"
            stroke={colors.red}
            strokeWidth="12"
            strokeLinecap="round"
          />
          <line
            x1="160"
            y1="40"
            x2="40"
            y2="160"
            stroke={colors.red}
            strokeWidth="12"
            strokeLinecap="round"
          />
        </svg>
      </div>

      {/* Title text */}
      <div
        style={{
          position: "absolute",
          bottom: 120,
          fontSize: 48,
          fontWeight: 700,
          color: colors.white,
          opacity: titleOpacity,
          fontFamily: fonts.sans,
        }}
      >
        GUI post-processing is{" "}
        <span style={{ color: colors.red }}>slow</span>
      </div>
    </AbsoluteFill>
  );
};
