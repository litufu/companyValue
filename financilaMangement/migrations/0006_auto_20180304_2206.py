# Generated by Django 2.0.2 on 2018-03-04 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financilaMangement', '0005_companylist_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancesheet',
            name='absrptn_of_dpsts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='吸收存款及同业存放'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='accnt_rcvd_in_advnc',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='预收款项'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='accnts_pybl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应付账款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='accnts_pybl_rnsrnc',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应付分保账款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='acnt_rcvbl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应收账款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='acnt_rcvbl_rnsrnc',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应收分保账款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='actng_sl_of_scrts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='代理买卖证券款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='actng_undrwrtng_scrts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='代理承销证券款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='atrbt_t_ownrs_eqty_of_prnt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='归属于母公司股东权益合计'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='avlbl_fr_sl_fnncl_assts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='可供出售金融资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='bll_rcvbl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应收票据'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='blls_pybl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应付票据'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='bnd_pybl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应付债券'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='brrwng_frm_th_cntrl_bnk',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='向中央银行借款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='by_bck_sl_of_fnncl_ast',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='买入返售金融资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='cash',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='货币资金'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='cnstrctn_in_prcss',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='在建工程'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='cptl_rsrv',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='资本公积'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='dfrrd_incm',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='递延收益'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='dfrrd_tx_assts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='递延所得税资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='dfrrd_tx_lblts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='递延所得税负债'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='drvtv_fncl_ast',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='衍生金融资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='drvtv_fnncl_lblts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='衍生金融负债'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='dspsl_of_fxd_assnts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='固定资产清理'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='dvdnd_pybl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应付股利'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='dvdnd_rcvbl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应收股利'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='emply_bnfts_pybl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应付职工薪酬'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='engnr_mtrls',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='工程物资'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='estmtd_lblty',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='预计负债'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='fncl_ast_hld_fr_trd',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='以公允价值计量且其变动计入当期损益的金融资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='fnncl_assts_sld_fr_rprchs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='卖出回购金融资产款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='fnncl_lblts_hld_fr_trd',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='以公允价值计量且其变动计入当期损益的金融负债'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='fxd_assts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='固定资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='gnrl_rsk_prprtn',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='一般风险准备'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='goodwill',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='商誉'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='hld_fr_sl_ast',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='持有待售资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='hld_fr_sl_dbt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='持有待售负债'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='hld_t_mtrty_invstmnts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='持有至到期投资'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='hndlng_fe_and_cmmssn',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应付手续费及佣金'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='intngbl_assts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='无形资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='intrst_pybl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应付利息'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='intrst_rcvbl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应收利息'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='invnstmnt_prpnrty',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='投资性房地产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='invntrs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='存货'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='lnd_t_bnk',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='拆出资金'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='lng_trm_accnt_pybl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='长期应付款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='lng_trm_dfrrd_expns',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='长期待摊费用'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='lng_trm_emply_bnfts_pybl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='长期应付职工薪酬'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='lng_trm_eqty_rcvbls',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='长期股权投资'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='lng_trm_ln',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='长期借款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='lng_trm_rcvbls',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='长期应收款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='lns_and_advncs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='发放委托贷款及垫款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='lns_frm_othr_bnks',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='拆入资金'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='lss_trsry_shr',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='减：库存股'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='mnrty_eqty',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='少数股东权益'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='nn_crnt_ast_ds_wthn_on_yr',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='一年内到期的非流动资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='nn_crnt_lblts_ds_wthn_on_yr',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='一年内到期的非流动负债'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='ol_and_gs_assts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='油气资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='othr_accnt_pybl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='其他应付款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='othr_accnt_rcvbl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='其他应收款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='othr_cmprhnsv_incm',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='其他综合收益'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='othr_crrnt_assts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='其他流动资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='othr_crrnt_lnlts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='其他流动负债'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='othr_eqty_instrmnts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='其他权益工具'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='othr_nn_crrnt_assts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='其他非流动资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='othr_nn_crrnt_lblts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='其他非流动负债'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='pd_n_cptl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='股本'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='prdctv_blgcl_assts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='生产性生物资产'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='prepayments',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='预付款项'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='r_d_expnss',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='开发支出'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='rcvbl_prm',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应收保费'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='rnsrnc_cntrct_reserve',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应收分保合同准备金'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='rsrv_fnd_fr_insrnc_cntrcts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='保险合同准备金'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='shrt_trm_ln',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='短期借款\u2005\u2005'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='spcfc_accnt_pybl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='专项应付款'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='spcl_rsrv',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='专项储备'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='srpls_rsrv',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='盈余公积'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='stlmnt_rsrv_fnd',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='结算备付金'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='ttl_assts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='资产总计'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='ttl_crrnt_assts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='流动资产合计'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='ttl_crrnt_lblts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='流动负债合计'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='ttl_lblts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='负债合计'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='ttl_lblts_and_ownrs_eqty',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='负债和股东权益总计'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='ttl_nn_crrnt_assts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='非流动资产合计'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='ttl_nn_crrnt_lblts',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='非流动负债合计'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='ttl_ownrs_eqty',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='股东权益合计'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='txs_pybl',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='应交税费'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='undstrbtd_prft',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=26, verbose_name='未分配利润'),
        ),
    ]
