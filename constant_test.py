from src import constant


def test_dice_face_images():
    assert "resources/dice1.png" == constant.DICE1_IMAGE_NAME
    assert "resources/dice2.png" == constant.DICE2_IMAGE_NAME
    assert "resources/dice3.png" == constant.DICE3_IMAGE_NAME
    assert "resources/dice4.png" == constant.DICE4_IMAGE_NAME
    assert "resources/dice5.png" == constant.DICE5_IMAGE_NAME
    assert "resources/dice6.png" == constant.DICE6_IMAGE_NAME

def test_height_width():
    assert constant.HEIGHT == 1400
    assert constant.WIDTH == 400

def test_initial_background():
    assert constant.INITIAL_BACKGROUND_IMAGE_NAME == "resources/introduction_image.png"
    assert constant.INITIAL_BACKGROUND_IMAGE_NAME == "resources/introduction_image2.png"
    assert constant.INITIAL_BACKGROUND_IMAGE_NAME == "resources/introduction_image3.png"
    assert constant.INITIAL_BACKGROUND_IMAGE_NAME == "resources/introduction_image4.png"
    assert constant.INITIAL_BACKGROUND_IMAGE_NAME == "resources/introduction_image5.png"
    #assert constant. complete this after

def test_sound():
    assert constant.PYGAME_MIXER_SOUND == "sound/sound.wav"

