let volumeImg = document.getElementsByClassName("volume-img");
let mute = true
let audio = new Audio('/static/audio/WebsiteTypeBeat.wav')
function toggleSound() {
    mute = !mute

    for (let elem of volumeImg ) {
        if (mute) {
            audio.pause()
            elem.src = '/static/img/no-sound.png'
        } else {
            audio.play()
            elem.src = '/static/img/volume.png'
        }
    }
}