//import { add_move_data } from "./data";
// Wait till the browser is ready to render the game (avoids glitches)
var gm
window.requestAnimationFrame(function () {
  gm = new GameManager(4, KeyboardInputManager, HTMLActuator, LocalStorageManager);
  gm.inputManager.on("move", add_move_data);
});
