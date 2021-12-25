package command

import (
	"fmt"

	"github.com/AudiusProject/audius-cli/src/utils"
)

func Trending() {
	fmt.Println(utils.Get("tracks/trending"))
}
