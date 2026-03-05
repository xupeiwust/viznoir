import { Composition } from "remotion";
import { ParapilotIntro } from "./ParapilotIntro";

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="parapilot-intro"
      component={ParapilotIntro}
      durationInFrames={30 * 55}
      fps={30}
      width={1920}
      height={1080}
    />
  );
};
