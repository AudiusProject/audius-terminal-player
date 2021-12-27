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

const (
	AppName                       = "audius-cli"
	AudiusAPIEndpointRetrievalURL = "https://api.audius.co"
)

// func PlayTrack(trackID string) {}

// go doesn't pass by reference by default so
// we must parse as a side-effect of fn
func bodyParser(unmarshaledAPIResponse *http.Response, responseData interface{}) (err error) {
	responseBody, err := io.ReadAll(unmarshaledAPIResponse.Body)
	if err != nil {
		return err
	}
	defer unmarshaledAPIResponse.Body.Close()

	err = json.Unmarshal(responseBody, &responseData)
	fmt.Println(responseData)
	if err != nil {
		return err
	}

	return
}

func Get(path string, queryOptions map[string]string, resp interface{}) (err error) {
	endpoint, err := GetAPIEndpoint()
	if err != nil {
		return err
	}

	queryOptions["app_name"] = AppName

	uri := fmt.Sprintf("%s/v1/%s", endpoint, path)

	response, err := http.Get(uri)
	if err != nil {
		return err
	}

	err = bodyParser(response, &resp)
	if err != nil {
		return err
	}

	return
}

func GetRandomIntInRange(bound int) (randomInt int) {
	return int(fastrand.PCG32Bounded(uint32(bound)))
}

func GetAPIEndpoint() (endpoint string, err error) {
	response, err := http.Get(AudiusAPIEndpointRetrievalURL)
	if err != nil {
		return "", err
	}
	// :wat:
	var activeAPIEndpointsTmp interface{}
	err = bodyParser(response, &activeAPIEndpointsTmp)

	// :wat-intensifies: :wiggle:
	activeAPIEndpointsTmp2 := activeAPIEndpointsTmp.(map[string]interface{})
	fmt.Println(activeAPIEndpointsTmp2["data"])
	if err != nil {
		return "", err
	}

	// activeAPIEndpoints := activeAPIEndpointsTmp2["data"]
	// randIndex := GetRandomIntInRange(len(activeAPIEndpoints))
	// return activeAPIEndpoints[randIndex], nil
}
