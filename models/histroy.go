package models

import (
	"encoding/json"

	"github.com/gobuffalo/pop/v5"
	"github.com/gobuffalo/validate/v3"
	"github.com/gofrs/uuid"
)

// Histroy is used by pop to map your histroys database table to your go code.
type Histroy struct {
	ID            int       `json:"id" db:"id"`
	MathOperation string    `json:"mathop" db:"mathop"`
	Result        string    `json:"result" db:"result"`
	Userid        uuid.UUID `json:"useruuid" db:"useruuid"`
}

// String is not required by pop and may be deleted
func (h Histroy) String() string {
	jh, _ := json.Marshal(h)
	return string(jh)
}

// Histroys is not required by pop and may be deleted
type Histroys []Histroy

// String is not required by pop and may be deleted
func (h Histroys) String() string {
	jh, _ := json.Marshal(h)
	return string(jh)
}

// Validate gets run every time you call a "pop.Validate*" (pop.ValidateAndSave, pop.ValidateAndCreate, pop.ValidateAndUpdate) method.
// This method is not required and may be deleted.
func (h *Histroy) Validate(tx *pop.Connection) (*validate.Errors, error) {
	return validate.NewErrors(), nil
}

// ValidateCreate gets run every time you call "pop.ValidateAndCreate" method.
// This method is not required and may be deleted.
func (h *Histroy) ValidateCreate(tx *pop.Connection) (*validate.Errors, error) {
	return validate.NewErrors(), nil
}

// ValidateUpdate gets run every time you call "pop.ValidateAndUpdate" method.
// This method is not required and may be deleted.
func (h *Histroy) ValidateUpdate(tx *pop.Connection) (*validate.Errors, error) {
	return validate.NewErrors(), nil
}
