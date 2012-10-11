package com.taobao.api.response;

import com.taobao.api.internal.mapping.ApiField;

import com.taobao.api.TaobaoResponse;

/**
 * TOP API: taobao.jipiao.agentorder.success response.
 * 
 * @author auto create
 * @since 1.0, null
 */
public class JipiaoAgentorderSuccessResponse extends TaobaoResponse {

	private static final long serialVersionUID = 6338133354229793826L;

	/** 
	 * 成功订单是否成功
	 */
	@ApiField("is_success")
	private Boolean isSuccess;

	public void setIsSuccess(Boolean isSuccess) {
		this.isSuccess = isSuccess;
	}
	public Boolean getIsSuccess( ) {
		return this.isSuccess;
	}

}
