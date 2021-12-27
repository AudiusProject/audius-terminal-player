package command

import (
	"fmt"

	"github.com/AudiusProject/audius-cli/src/utils"
)

func Trending() error {
	var queryOptions = map[string]string{}
	var resp interface{}
	err := utils.Get("tracks/trending", queryOptions, &resp)
	if err != nil {
		return err
	}

	fmt.Println(resp)
	return nil
}
