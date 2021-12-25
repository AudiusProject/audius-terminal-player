package fastrand

import (
	"crypto/rand"
	"encoding/binary"
)

const inc = uint64(0xda3e39cb94b95bdb)

var randomBytes, _ = GenerateRandomBytes(8)
var state = binary.BigEndian.Uint64(randomBytes)

// GenerateRandomBytes returns securely generated random bytes.
func GenerateRandomBytes(n int) ([]byte, error) {
	b := make([]byte, n)
	_, err := rand.Read(b)
	if err != nil {
		return nil, err
	}

	return b, nil
}

// PCG32 returns a random unsigned 32 bit integer using PCG.
func PCG32() uint32 {
	oldstate := uint64(state)
	state = (oldstate*uint64(0x5851f42d4c957f2d) + inc)
	xorshifted := uint32(((oldstate >> 18) ^ oldstate) >> 27)
	rot := uint32(oldstate >> 59)
	return (xorshifted >> rot) | (xorshifted << (-rot & 31))
}

// PCG32Bounded returns a random unsigned 32 bit integer in the interval [0, bound) using PCG.
func PCG32Bounded(bound uint32) uint32 {
	bound64 := uint64(bound)
	random32bits := uint64(PCG32())
	multiresult := random32bits * bound64
	leftover := uint32(multiresult)

	if leftover < bound {
		threshold := -bound % bound
		for leftover < threshold {
			random32bits = uint64(PCG32())
			multiresult = random32bits * bound64
			leftover = uint32(multiresult)
		}
	}

	return uint32(multiresult >> 32)
}
