import React, {useState, useEffect} from "react";

function App() {

    const [pedestrianVolume, setPedestrianVolume] = useState([]);

    const [bicycleVolume, setBicycleVolume] = useState([]);

    useEffect(() => {
        // fetch pedestrian volume
        fetch("/volume/pedestrian")
            .then((res) => res.json()
                .then((volume) => {
                    setPedestrianVolume(volume);
                })
            );
        // fetch bicycle volume
        fetch("/volume/bicycle")
            .then((res) => res.json()
                .then((volume) => {
                    setBicycleVolume(volume);
                })
            );

    }, []);
    return (
        <div className="App">
            <header className="App-header">
                <p>Pedestrian Volume</p>
                <div>{JSON.stringify(pedestrianVolume)}</div>
                <p>Bicycle Volume</p>
                <div>{JSON.stringify(bicycleVolume)}</div>
            </header>
        </div>
    );
}

export default App;
