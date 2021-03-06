package com.taobao.api.domain;

import com.taobao.api.TaobaoObject;
import com.taobao.api.internal.mapping.ApiField;

/**
 * 本地生活垂直市场数据结构，修改宝贝时在参数empty_fields里设置locality_life可删除所有电子凭证信息
 *
 * @author auto create
 * @since 1.0, null
 */
public class LocalityLife extends TaobaoObject {

	private static final long serialVersionUID = 8431419468842759624L;

	/**
	 * 电子交易凭证有效期，有三种格式：
如果有效期为起止日期类型，此值为2012-08-06,2012-08-16 
如果有效期为【购买成功日 至】类型则格式为2012-08-16
如果有效期为天数类型则格式为15
	 */
	@ApiField("expirydate")
	private String expirydate;

	/**
	 * 格式为 
码商id:nick
	 */
	@ApiField("merchant")
	private String merchant;

	/**
	 * 网点ID,在参数empty_fields里设置locality_life.network_id可删除网点ID
	 */
	@ApiField("network_id")
	private String networkId;

	/**
	 * 退款比例，百分比%前的数字，1-100的正整数值；在参数empty_fields里设置locality_life.refund_ratio可删除退款比例
	 */
	@ApiField("refund_ratio")
	private Long refundRatio;

	/**
	 * 核销打款:1代表核销打款,0代表非核销打款;
在参数empty_fields里设置locality_life.verification可删除核销打款
	 */
	@ApiField("verification")
	private String verification;

	public String getExpirydate() {
		return this.expirydate;
	}
	public void setExpirydate(String expirydate) {
		this.expirydate = expirydate;
	}

	public String getMerchant() {
		return this.merchant;
	}
	public void setMerchant(String merchant) {
		this.merchant = merchant;
	}

	public String getNetworkId() {
		return this.networkId;
	}
	public void setNetworkId(String networkId) {
		this.networkId = networkId;
	}

	public Long getRefundRatio() {
		return this.refundRatio;
	}
	public void setRefundRatio(Long refundRatio) {
		this.refundRatio = refundRatio;
	}

	public String getVerification() {
		return this.verification;
	}
	public void setVerification(String verification) {
		this.verification = verification;
	}

}
