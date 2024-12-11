package api

import "net/http"

type Api interface {
	GetSumishinSBIBankLatest(w http.ResponseWriter, r *http.Request)
	GetRakutenBankLatest(w http.ResponseWriter, r *http.Request)
	GetMitsuisumitomoBankLatest(w http.ResponseWriter, r *http.Request)
	GetSBIShinseiBankLatest(w http.ResponseWriter, r *http.Request)
	GetSBIStockLatest(w http.ResponseWriter, r *http.Request)
	GetRakutenStockLatest(w http.ResponseWriter, r *http.Request)
	GetSBIBenefitSystemsLatest(w http.ResponseWriter, r *http.Request)
	GetMitsuisumitomoCreditCardLatest(w http.ResponseWriter, r *http.Request)
	GetRakutenCreditCardLatest(w http.ResponseWriter, r *http.Request)
}

type ApiImpl struct{}

func New() Api {
	return &ApiImpl{}
}

// bank

func (a *ApiImpl) GetSumishinSBIBankLatest(w http.ResponseWriter, r *http.Request) {}

func (a *ApiImpl) GetRakutenBankLatest(w http.ResponseWriter, r *http.Request) {}

func (a *ApiImpl) GetMitsuisumitomoBankLatest(w http.ResponseWriter, r *http.Request) {}

func (a *ApiImpl) GetSBIShinseiBankLatest(w http.ResponseWriter, r *http.Request) {}

// stock

func (a *ApiImpl) GetSBIStockLatest(w http.ResponseWriter, r *http.Request) {
	// crowling部分はpythonにつなげるはず
}

func (a *ApiImpl) GetRakutenStockLatest(w http.ResponseWriter, r *http.Request) {}

func (a *ApiImpl) GetSBIBenefitSystemsLatest(w http.ResponseWriter, r *http.Request) {}

// credit card

func (a *ApiImpl) GetMitsuisumitomoCreditCardLatest(w http.ResponseWriter, r *http.Request) {}

func (a *ApiImpl) GetRakutenCreditCardLatest(w http.ResponseWriter, r *http.Request) {}
