from django.db import models

# Create your models here.

class CompanyList(models.Model):
    code = models.CharField('公司代码',max_length=10,primary_key=True)
    name = models.CharField('公司名称',max_length=10)
    area = models.CharField('所属地区',max_length=10,default='北京')
    industry = models.CharField('所属行业',max_length=10)
    timeToMarket = models.DateField('上市时间')

    class Meta:
        verbose_name = "公司列表"
        verbose_name_plural = "公司列表清单"

    def __str__(self):
        return self.code

class ReportType(models.Model):
    type = models.CharField(verbose_name='报表类型代码',max_length=1,primary_key=True)
    name = models.CharField(verbose_name='报表类型名称',max_length=10)

    class Meta:
        verbose_name = "报表类型"
        verbose_name_plural = "报表类型清单"

    def __str__(self):
        return self.name

class BalanceSheet(models.Model):
    stk_cd = models.ForeignKey(CompanyList, on_delete=models.CASCADE,verbose_name='股票代码')
    acc_per = models.DateField('会计期间')
    typ_rep = models.ForeignKey(ReportType, on_delete=models.CASCADE,verbose_name='报表类型')
    cash = models.DecimalField('货币资金', max_digits=26, decimal_places=2, default=0.00)
    stlmnt_rsrv_fnd = models.DecimalField('结算备付金', max_digits=26, decimal_places=2, default=0.00)
    lnd_t_bnk = models.DecimalField('拆出资金', max_digits=26, decimal_places=2, default=0.00)
    fncl_ast_hld_fr_trd = models.DecimalField('以公允价值计量且其变动计入当期损益的金融资产', max_digits=26, decimal_places=2, default=0.00)
    drvtv_fncl_ast = models.DecimalField('衍生金融资产', max_digits=26, decimal_places=2, default=0.00)
    bll_rcvbl = models.DecimalField('应收票据', max_digits=26, decimal_places=2, default=0.00)
    acnt_rcvbl = models.DecimalField('应收账款', max_digits=26, decimal_places=2, default=0.00)
    prepayments = models.DecimalField('预付款项', max_digits=26, decimal_places=2, default=0.00)
    rcvbl_prm = models.DecimalField('应收保费', max_digits=26, decimal_places=2, default=0.00)
    acnt_rcvbl_rnsrnc = models.DecimalField('应收分保账款', max_digits=26, decimal_places=2, default=0.00)
    rnsrnc_cntrct_reserve = models.DecimalField('应收分保合同准备金', max_digits=26, decimal_places=2, default=0.00)
    intrst_rcvbl = models.DecimalField('应收利息', max_digits=26, decimal_places=2, default=0.00)
    dvdnd_rcvbl = models.DecimalField('应收股利', max_digits=26, decimal_places=2, default=0.00)
    othr_accnt_rcvbl = models.DecimalField('其他应收款', max_digits=26, decimal_places=2, default=0.00)
    by_bck_sl_of_fnncl_ast = models.DecimalField('买入返售金融资产', max_digits=26, decimal_places=2, default=0.00)
    invntrs = models.DecimalField('存货', max_digits=26, decimal_places=2, default=0.00)
    hld_fr_sl_ast = models.DecimalField('持有待售资产', max_digits=26, decimal_places=2, default=0.00)
    nn_crnt_ast_ds_wthn_on_yr = models.DecimalField('一年内到期的非流动资产', max_digits=26, decimal_places=2, default=0.00)
    othr_crrnt_assts = models.DecimalField('其他流动资产', max_digits=26, decimal_places=2, default=0.00)
    ttl_crrnt_assts = models.DecimalField('流动资产合计', max_digits=26, decimal_places=2, default=0.00)
    lns_and_advncs = models.DecimalField('发放委托贷款及垫款', max_digits=26, decimal_places=2, default=0.00)
    avlbl_fr_sl_fnncl_assts = models.DecimalField('可供出售金融资产', max_digits=26, decimal_places=2, default=0.00)
    hld_t_mtrty_invstmnts = models.DecimalField('持有至到期投资', max_digits=26, decimal_places=2, default=0.00)
    lng_trm_rcvbls = models.DecimalField('长期应收款', max_digits=26, decimal_places=2, default=0.00)
    lng_trm_eqty_rcvbls = models.DecimalField('长期股权投资', max_digits=26, decimal_places=2, default=0.00)
    invnstmnt_prpnrty = models.DecimalField('投资性房地产', max_digits=26, decimal_places=2, default=0.00)
    fxd_assts = models.DecimalField('固定资产', max_digits=26, decimal_places=2, default=0.00)
    cnstrctn_in_prcss = models.DecimalField('在建工程', max_digits=26, decimal_places=2, default=0.00)
    engnr_mtrls = models.DecimalField('工程物资', max_digits=26, decimal_places=2, default=0.00)
    dspsl_of_fxd_assnts = models.DecimalField('固定资产清理', max_digits=26, decimal_places=2, default=0.00)
    prdctv_blgcl_assts = models.DecimalField('生产性生物资产', max_digits=26, decimal_places=2, default=0.00)
    ol_and_gs_assts = models.DecimalField('油气资产', max_digits=26, decimal_places=2, default=0.00)
    intngbl_assts = models.DecimalField('无形资产', max_digits=26, decimal_places=2, default=0.00)
    r_d_expnss = models.DecimalField('开发支出', max_digits=26, decimal_places=2, default=0.00)
    goodwill = models.DecimalField('商誉', max_digits=26, decimal_places=2, default=0.00)
    lng_trm_dfrrd_expns = models.DecimalField('长期待摊费用', max_digits=26, decimal_places=2, default=0.00)
    dfrrd_tx_assts = models.DecimalField('递延所得税资产', max_digits=26, decimal_places=2, default=0.00)
    othr_nn_crrnt_assts = models.DecimalField('其他非流动资产', max_digits=26, decimal_places=2, default=0.00)
    ttl_nn_crrnt_assts = models.DecimalField('非流动资产合计', max_digits=26, decimal_places=2, default=0.00)
    ttl_assts = models.DecimalField('资产总计', max_digits=26, decimal_places=2, default=0.00)
    shrt_trm_ln = models.DecimalField('短期借款  ', max_digits=26, decimal_places=2, default=0.00)
    brrwng_frm_th_cntrl_bnk = models.DecimalField('向中央银行借款', max_digits=26, decimal_places=2, default=0.00)
    absrptn_of_dpsts = models.DecimalField('吸收存款及同业存放', max_digits=26, decimal_places=2, default=0.00)
    lns_frm_othr_bnks = models.DecimalField('拆入资金', max_digits=26, decimal_places=2, default=0.00)
    fnncl_lblts_hld_fr_trd = models.DecimalField('以公允价值计量且其变动计入当期损益的金融负债', max_digits=26, decimal_places=2,
                                                 default=0.00)
    drvtv_fnncl_lblts = models.DecimalField('衍生金融负债', max_digits=26, decimal_places=2, default=0.00)
    blls_pybl = models.DecimalField('应付票据', max_digits=26, decimal_places=2, default=0.00)
    accnts_pybl = models.DecimalField('应付账款', max_digits=26, decimal_places=2, default=0.00)
    accnt_rcvd_in_advnc = models.DecimalField('预收款项', max_digits=26, decimal_places=2, default=0.00)
    fnncl_assts_sld_fr_rprchs = models.DecimalField('卖出回购金融资产款', max_digits=26, decimal_places=2, default=0.00)
    hndlng_fe_and_cmmssn = models.DecimalField('应付手续费及佣金', max_digits=26, decimal_places=2, default=0.00)
    emply_bnfts_pybl = models.DecimalField('应付职工薪酬', max_digits=26, decimal_places=2, default=0.00)
    txs_pybl = models.DecimalField('应交税费', max_digits=26, decimal_places=2, default=0.00)
    intrst_pybl = models.DecimalField('应付利息', max_digits=26, decimal_places=2, default=0.00)
    dvdnd_pybl = models.DecimalField('应付股利', max_digits=26, decimal_places=2, default=0.00)
    othr_accnt_pybl = models.DecimalField('其他应付款', max_digits=26, decimal_places=2, default=0.00)
    accnts_pybl_rnsrnc = models.DecimalField('应付分保账款', max_digits=26, decimal_places=2, default=0.00)
    rsrv_fnd_fr_insrnc_cntrcts = models.DecimalField('保险合同准备金', max_digits=26, decimal_places=2, default=0.00)
    actng_sl_of_scrts = models.DecimalField('代理买卖证券款', max_digits=26, decimal_places=2, default=0.00)
    actng_undrwrtng_scrts = models.DecimalField('代理承销证券款', max_digits=26, decimal_places=2, default=0.00)
    hld_fr_sl_dbt = models.DecimalField('持有待售负债', max_digits=26, decimal_places=2, default=0.00)
    nn_crnt_lblts_ds_wthn_on_yr = models.DecimalField('一年内到期的非流动负债', max_digits=26, decimal_places=2, default=0.00)
    othr_crrnt_lnlts = models.DecimalField('其他流动负债', max_digits=26, decimal_places=2, default=0.00)
    ttl_crrnt_lblts = models.DecimalField('流动负债合计', max_digits=26, decimal_places=2, default=0.00)
    lng_trm_ln = models.DecimalField('长期借款', max_digits=26, decimal_places=2, default=0.00)
    bnd_pybl = models.DecimalField('应付债券', max_digits=26, decimal_places=2, default=0.00)
    lng_trm_accnt_pybl = models.DecimalField('长期应付款', max_digits=26, decimal_places=2, default=0.00)
    lng_trm_emply_bnfts_pybl = models.DecimalField('长期应付职工薪酬', max_digits=26, decimal_places=2, default=0.00)
    spcfc_accnt_pybl = models.DecimalField('专项应付款', max_digits=26, decimal_places=2, default=0.00)
    estmtd_lblty = models.DecimalField('预计负债', max_digits=26, decimal_places=2, default=0.00)
    dfrrd_incm = models.DecimalField('递延收益', max_digits=26, decimal_places=2, default=0.00)
    dfrrd_tx_lblts = models.DecimalField('递延所得税负债', max_digits=26, decimal_places=2, default=0.00)
    othr_nn_crrnt_lblts = models.DecimalField('其他非流动负债', max_digits=26, decimal_places=2, default=0.00)
    ttl_nn_crrnt_lblts = models.DecimalField('非流动负债合计', max_digits=26, decimal_places=2, default=0.00)
    ttl_lblts = models.DecimalField('负债合计', max_digits=26, decimal_places=2, default=0.00)
    pd_n_cptl = models.DecimalField('股本', max_digits=26, decimal_places=2, default=0.00)
    othr_eqty_instrmnts = models.DecimalField('其他权益工具', max_digits=26, decimal_places=2, default=0.00)
    cptl_rsrv = models.DecimalField('资本公积', max_digits=26, decimal_places=2, default=0.00)
    lss_trsry_shr = models.DecimalField('减：库存股', max_digits=26, decimal_places=2, default=0.00)
    othr_cmprhnsv_incm = models.DecimalField('其他综合收益', max_digits=26, decimal_places=2, default=0.00)
    spcl_rsrv = models.DecimalField('专项储备', max_digits=26, decimal_places=2, default=0.00)
    srpls_rsrv = models.DecimalField('盈余公积', max_digits=26, decimal_places=2, default=0.00)
    gnrl_rsk_prprtn = models.DecimalField('一般风险准备', max_digits=26, decimal_places=2, default=0.00)
    undstrbtd_prft = models.DecimalField('未分配利润', max_digits=26, decimal_places=2, default=0.00)
    atrbt_t_ownrs_eqty_of_prnt = models.DecimalField('归属于母公司股东权益合计', max_digits=26, decimal_places=2, default=0.00)
    mnrty_eqty = models.DecimalField('少数股东权益', max_digits=26, decimal_places=2, default=0.00)
    ttl_ownrs_eqty = models.DecimalField('股东权益合计', max_digits=26, decimal_places=2, default=0.00)
    ttl_lblts_and_ownrs_eqty = models.DecimalField('负债和股东权益总计', max_digits=26, decimal_places=2, default=0.00)

    def check_logic(self):
        return self.ttl_lblts_and_ownrs_eqty == self.ttl_assts











