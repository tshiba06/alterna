package handler

import "context"

type Handler interface {
	SaveSumishin(ctx context.Context) error
}

type HandlerImpl struct {
}

func New() Handler {
	return &HandlerImpl{}
}

func (h *HandlerImpl) SaveSumishin(ctx context.Context) error {
	return nil
}
