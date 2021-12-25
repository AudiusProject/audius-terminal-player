// util that sends an API request to endpoint

// util that takes an mp3 file and streams it through terminal

package utils

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"

	"github.com/cheran-senthil/fastrand" // cheran is amazing
)

func PlayTrack(trackID string) {}

func Get(path string) (resp *http.Response, err error) {
	endpoint, err := GetAPIEndpoint()
	if err != nil {
		return nil, err
	}
	uri := endpoint + "/v1/" + path
	fmt.Println(uri)
	return http.Get(uri)
}

func GetAPIEndpoint() (endpoint string, err error) {
	response, err := http.Get("https://api.audius.co")

	if err != nil {
		return "", err
	}

	responseData, err := io.ReadAll(response.Body)
	if err != nil {
		return "", err
	}

	var data map[string][]string
	err = json.Unmarshal(responseData, &data)
	if err != nil {
		return "", err
	}

	randIndex := fastrand.PCG32Bounded(uint32(len(data["data"])))
	fmt.Println(data["data"][randIndex])
	return data["data"][randIndex], nil
}
