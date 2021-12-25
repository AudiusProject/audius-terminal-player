package cli

// cli
import (
	"fmt"

	"github.com/AudiusProject/audius-cli/src/command"
	log "github.com/sirupsen/logrus"
	"github.com/spf13/cobra"
)

var (
	args    = 1
	rootCmd = &cobra.Command{
		Use:   "audius [flags]",
		Short: "CLI to play the best music in the world 🎧",
		Args:  cobra.ExactArgs(args),
		Run:   run,
	}
)

func run(cmd *cobra.Command, args []string) {
	fmt.Println(cmd, args)
}

func Execute() {
	log.Debug("start")
	command.Trending()
}
